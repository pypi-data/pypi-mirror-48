import time
import itertools
import logging
import asyncio
from collections import deque

log = logging.getLogger('peewee_syncer')


class LastOffsetQueryIterator:
    def __init__(self, i, row_output_fun, key_fun, is_unique_key=False):
        self.iterator = i
        self.n = 0
        self.row_output_fun = row_output_fun
        self.last_updates = deque([None], maxlen=2)
        self.key_fun = key_fun
        self.is_unique_key = is_unique_key

    def get_last_offset(self, limit):
        # log.debug("Offsets {} n={} limit={}".format(self.last_updates, self.n, limit))
        if self.n == limit and not self.is_unique_key:
            return self.last_updates[0]
        else:
            return self.last_updates[-1]

    def iterate(self):
        for row in self.iterator:
            self.n = self.n + 1

            value = self.key_fun(row)
            if self.last_updates[-1] != value:
                self.last_updates.append(value)

            output = self.row_output_fun(row)
            if output:
                yield output


class Processor:
    def __init__(self, sync_manager, it_function, process_function, sleep_duration=3):
        self.it_function = it_function
        self.process_function = process_function
        self.sync_manager = sync_manager
        self.sleep_duration = sleep_duration

    @classmethod
    def should_stop(cls, i, n):
        if i > 0 and n == i:
            log.debug("Stopping after iteration {}".format(n))
            return True
        return False

    def get_last_offset_and_iterator(self, limit):
        last_offset = self.sync_manager.get_last_offset()

        it = self.it_function(since=last_offset['value'], limit=limit)

        return last_offset, it

    def save(self):
        with self.sync_manager.get_db().connection_context():
            self.sync_manager.save()

    def process(self, limit, i):

        for n in itertools.count():

            if self.should_stop(i=i, n=n):
                break

            last_offset, it = self.get_last_offset_and_iterator(limit=limit)

            if not it:
                break

            self.process_function(it.iterate())

            if self.sync_manager.is_test_run:
                log.debug("Stopping after iteration (test in progress). Processed {} records".format(it.n))
                break

            final_offset = it.get_last_offset(limit=limit)

            if it.n == 0:
                log.debug("Caught up, sleeping..")
                time.sleep(self.sleep_duration)
            else:
                log.debug(
                    "Processed records n={} offset={}".format(it.n, final_offset if final_offset else "unchanged"),
                    extra={'n': it.n, 'offset': final_offset})

                if final_offset != last_offset['value']:
                    if final_offset:
                        self.sync_manager.set_last_offset(final_offset, 0)
                else:
                    time.sleep(self.sleep_duration)
                    # todo: if behind current time then abort on second attempt
                    # this would prevent stuck in loop due to bulk updates
                    log.warning("Final offset remains unchanged")

                self.save()

        log.info("Completed processing")


class AsyncProcessor(Processor):

    def __init__(self, object, sync_manager, it_function, process_function, sleep_duration=3):
        super().__init__(sync_manager=sync_manager, it_function=it_function, process_function=process_function, sleep_duration=sleep_duration)
        self.object = object

    async def get_last_offset_and_iterator(self, limit):

        last_offset = self.sync_manager.get_last_offset()

        it = await self.it_function(since=last_offset['value'], limit=limit)

        return last_offset, it

    async def save(self):
        await self.object.update(self.sync_manager)

    async def process(self, limit, i):

        for n in itertools.count():

            if self.should_stop(i=i, n=n):
                break

            last_offset, it = await self.get_last_offset_and_iterator(limit=limit)

            if not it:
                break

            await self.process_function(it.iterate())

            if self.sync_manager.is_test_run:
                log.debug("Stopping after iteration (test in progress). Processed {} records".format(it.n))
                break

            final_offset = it.get_last_offset(limit=limit)

            if it.n == 0:
                log.info("Caught up, sleeping..")
                await asyncio.sleep(self.sleep_duration)

            else:
                log.debug("Processed records {} - {} / {}".format("" if final_offset else "unchanged", it.n, final_offset),
                               extra={'n': it.n, 'offset': final_offset})

                if final_offset and final_offset != last_offset['value']:
                    # todo: sleep based on % of limit
                    if final_offset:
                        self.sync_manager.set_last_offset(final_offset, 0)
                else:
                    await asyncio.sleep(self.sleep_duration)
                    # todo: if behind current time then abort on second attempt
                    # this would prevent stuck in loop due to bulk updates
                    log.warning("Final offset remains unchaged")

                await self.save()

        log.info("Completed importing")

