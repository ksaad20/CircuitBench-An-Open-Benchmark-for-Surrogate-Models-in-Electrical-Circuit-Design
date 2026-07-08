"""
efficiency.py
=============

Efficiency metrics for CircuitBench.

Provides metrics for computational efficiency,
resource utilization, throughput, scalability,
and hardware performance.

Author: CircuitBench Development Team
License: Apache 2.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Sequence

import time
import numpy as np

__all__ = [
    "EfficiencyResult",
    "efficiency_score",
    "compute_efficiency",
    "throughput_efficiency",
    "latency_efficiency",
    "memory_efficiency",
    "energy_efficiency",
    "accuracy_efficiency",
    "parameter_efficiency",
    "compute_per_parameter",
    "flops_per_second",
]

"""
Efficiency metrics.
"""

@dataclass(frozen=True)
class EfficiencyResult:
    """
    Container for efficiency statistics.
    """

    score: float
    metric: str
    unit: str

    def as_dict(self) -> Dict[str, float | str]:
        return {
            "score": self.score,
            "metric": self.metric,
            "unit": self.unit,
        }

def _validate_positive(value: float, name: str) -> None:
    """
    Validate that a value is positive.
    """

    if value <= 0:
        raise ValueError(f"{name} must be positive.")

def efficiency_score(
    useful_work: float,
    total_cost: float,
) -> float:
    """
    Compute generic efficiency score.

    Efficiency = useful_work / total_cost
    """

    _validate_positive(useful_work, "useful_work")
    _validate_positive(total_cost, "total_cost")

    return float(useful_work / total_cost)

def compute_efficiency(
    operations: float,
    execution_time: float,
) -> float:
    """
    Operations per second.
    """

    _validate_positive(operations, "operations")
    _validate_positive(execution_time, "execution_time")

    return float(
        operations / execution_time
    )

def throughput_efficiency(
    throughput: float,
    theoretical_max: float,
) -> float:
    """
    Throughput utilization.
    """

    _validate_positive(throughput, "throughput")
    _validate_positive(theoretical_max, "theoretical_max")

    return float(
        throughput / theoretical_max
    )

def latency_efficiency(
    ideal_latency: float,
    measured_latency: float,
) -> float:
    """
    Latency efficiency.

    Values closer to 1 are better.
    """

    _validate_positive(ideal_latency, "ideal_latency")
    _validate_positive(measured_latency, "measured_latency")

    return float(
        ideal_latency /
        measured_latency
    )

def memory_efficiency(
    minimum_memory: float,
    actual_memory: float,
) -> float:
    """
    Memory efficiency.
    """

    _validate_positive(minimum_memory, "minimum_memory")
    _validate_positive(actual_memory, "actual_memory")

    return float(
        minimum_memory /
        actual_memory
    )

def accuracy_efficiency(
    accuracy: float,
    latency: float,
) -> float:
    """
    Accuracy per unit latency.
    """

    _validate_positive(latency, "latency")

    return float(
        accuracy /
        latency
    )

def parameter_efficiency(
    accuracy: float,
    parameters: int,
) -> float:
    """
    Accuracy per model parameter.
    """

    _validate_positive(parameters, "parameters")

    return float(
        accuracy /
        parameters
    )

def compute_per_parameter(
    flops: float,
    parameters: int,
) -> float:
    """
    FLOPs per parameter.
    """

    _validate_positive(flops, "flops")
    _validate_positive(parameters, "parameters")

    return float(
        flops /
        parameters
)

def flops_per_second(
    flops: float,
    seconds: float,
) -> float:
    """
    Compute FLOPs per second.
    """

    _validate_positive(flops, "flops")
    _validate_positive(seconds, "seconds")

    return float(
        flops /
        seconds
    )

def throughput(samples, seconds):
    return samples / seconds


def samples_per_second(samples, runtime):
    return samples / runtime


def speedup(serial, parallel):
    return serial / parallel


def efficiency(speedup_value, processors):
    return speedup_value / processors

__all__ = [
    "efficiency_score",
    "compute_efficiency",
    "throughput_efficiency",
    "latency_efficiency",
    "memory_efficiency",
    "energy_efficiency",
    "accuracy_efficiency",
    "parameter_efficiency",
    "compute_per_parameter",
    "flops_per_second",
    "operations_per_second",
    "samples_per_second",
    "images_per_second",
    "tokens_per_second",
    "examples_per_second",
    "batch_efficiency",
    "scaling_efficiency",
    "parallel_efficiency",
    "speedup",
    "strong_scaling_efficiency",
    "weak_scaling_efficiency",
    "utilization",
    "resource_utilization",
    "hardware_efficiency",
    "compute_utilization",
    "io_efficiency",
    "cache_efficiency",
    "bandwidth_efficiency",
    "pipeline_efficiency",
    "overall_efficiency",
    "efficiency_summary",
    "efficiency_dataframe",
    "efficiency_report",
    "normalize_efficiency",
    "weighted_efficiency",
]
