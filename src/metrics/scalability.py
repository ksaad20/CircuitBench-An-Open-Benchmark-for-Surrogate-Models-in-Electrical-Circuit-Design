"""
Scalability metrics.
"""

from __future__ import annotations

import numpy as np


def speedup(serial_time,
            parallel_time):

    return serial_time / parallel_time


def efficiency(serial_time,
               parallel_time,
               processors):

    return speedup(serial_time,
                   parallel_time) / processors


def strong_scaling(serial_times,
                   parallel_times):

    serial_times = np.asarray(serial_times)

    parallel_times = np.asarray(parallel_times)

    return serial_times / parallel_times


def weak_scaling(times):

    times = np.asarray(times)

    return times[0] / times


def runtime_scaling(samples,
                    runtime):

    return runtime / samples


def memory_scaling(samples,
                   memory):

    return memory / samples


def parameter_scaling(parameters,
                      runtime):

    return runtime / parameters


def scaling_index(runtime):

    runtime = np.asarray(runtime)

    return runtime[-1] / runtime[0]


def efficiency_curve(serial,
                     parallel):

    return np.asarray(serial) / np.asarray(parallel)
