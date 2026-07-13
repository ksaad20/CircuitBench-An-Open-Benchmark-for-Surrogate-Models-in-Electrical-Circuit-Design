"""
CircuitBench Benchmark Runner

Core benchmark execution engine.

Author: CircuitBench
License: Apache-2.0
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class BenchmarkResult:
    """Stores the result of a single benchmark execution."""

    model_name: str
    dataset_name: str
    metrics: Dict[str, float]
    runtime: float = 0.0
    memory: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class BenchmarkRunner:
    """
    Main benchmarking engine.

    Responsible for

    - model registration
    - dataset registration
    - metric evaluation
    - report generation
    - callbacks
    """

    def __init__(
        self,
        metrics: Optional[List[Callable]] = None,
        dataset: Any = None,
        model: Any = None,
        random_state: Optional[int] = None,
        output_directory: Optional[str] = None,
        callbacks: Optional[List[Callable]] = None,
    ):

        self.metrics = metrics or []
        self.datasets: List[Any] = []
        self.models: List[Any] = []
        self.results: List[BenchmarkResult] = []

        self.random_state = random_state
        self.dataset = dataset
        self.model = model

        self.output_directory = Path(output_directory or "benchmark_results")

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.callbacks = callbacks or []

        self.history: List[Dict[str, Any]] = []

        self.start_time = None

        logger.info("BenchmarkRunner initialized.")

        if dataset is not None:
            self.datasets.append(dataset)

        if model is not None:
            self.models.append(model)
