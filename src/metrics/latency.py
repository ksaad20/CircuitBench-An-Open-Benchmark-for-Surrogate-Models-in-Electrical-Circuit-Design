"""
Latency measurements.
"""

import time


def measure(function, *args, **kwargs):
    start = time.perf_counter()
    function(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def average_latency(function, n=100, *args, **kwargs):
    values = []
    for _ in range(n):
        values.append(measure(function, *args, **kwargs))
    return sum(values) / len(values)
