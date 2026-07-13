"""
CircuitBench Benchmark Framework.
"""

from __future__ import annotations

from .runner import BenchmarkRunner
from .benchmark_runner import BenchmarkRunner as LegacyBenchmarkRunner
from .benchmark_suite import BenchmarkSuite
from .experiment import Experiment
from .experiment_manager import ExperimentManager
from .leaderboard import Leaderboard

AVAILABLE_BENCHMARKS = [
    "classification",
    "regression",
    "simulation",
    "optimization",
]

__all__ = [
    "BenchmarkRunner",
    "LegacyBenchmarkRunner",
    "BenchmarkSuite",
    "Experiment",
    "ExperimentManager",
    "Leaderboard",
    "AVAILABLE_BENCHMARKS",
]
