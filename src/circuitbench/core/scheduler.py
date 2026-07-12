"""
Task scheduler.
"""

from concurrent.futures import ThreadPoolExecutor


class Scheduler:
    def __init__(self, max_workers=4):

        self.max_workers = max_workers

    def submit(self, function, *args, **kwargs):

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future = executor.submit(function, *args, **kwargs)

            return future.result()

    def map(self, function, iterable):

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(function, iterable))
