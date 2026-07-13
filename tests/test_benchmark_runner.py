"""
CircuitBench Benchmark Runner.

Core benchmarking framework used throughout CircuitBench.
"""

from __future__ import annotations

import json
import os
import platform
import pickle
import sys
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd


class BenchmarkRunner:
    """
    Main benchmark runner.
    """

    def __init__(
        self,
        name: str = "CircuitBench",
        output_directory: str | os.PathLike = ".",
        random_state: int | None = None,
    ) -> None:
        self.name = name
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

        self.random_state = random_state

        if random_state is not None:
            np.random.seed(random_state)

        # Registered objects
        self.datasets: list[Any] = []
        self.models: list[Any] = []
        self.metrics: dict[str, Callable] = {}

        # Results
        self.results: list[dict[str, Any]] = []
        self.history: list[dict[str, Any]] = []
        self.statistics: dict[str, Any] = {}

        # Integrations
        self.leaderboard = None
        self.report = None
        self.experiment = None

        # Callbacks
        self.callbacks: list[Callable] = []

        # Cross validation
        self.cv_strategy: str | None = None
        self.cv_folds: int | None = None

        # Timing
        self._timer_start: float | None = None

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def number_of_models(self) -> int:
        return len(self.models)

    @property
    def number_of_datasets(self) -> int:
        return len(self.datasets)

    @property
    def number_of_metrics(self) -> int:
        return len(self.metrics)

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def add_dataset(self, dataset: Any) -> None:
        self.datasets.append(dataset)

    def add_model(self, model: Any) -> None:
        self.models.append(model)

    def add_metric(
        self,
        name: str,
        function: Callable,
    ) -> None:
        self.metrics[name] = function

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self) -> bool:
        if not self.datasets:
            raise RuntimeError("No datasets registered.")

        if not self.models:
            raise RuntimeError("No models registered.")

        if not self.metrics:
            raise RuntimeError("No metrics registered.")

        return True

    # ------------------------------------------------------------------
    # Inspection
    # ------------------------------------------------------------------

    def inspect_dataset(self, dataset: Any) -> dict[str, Any]:
        return {
            "samples": len(dataset.X_train),
            "targets": len(dataset.y_train),
            "features": dataset.X_train.shape[1],
        }

    def inspect_model(self, model: Any) -> dict[str, Any]:
        return {
            "name": getattr(
                model,
                "name",
                model.__class__.__name__,
            ),
            "type": model.__class__.__name__,
        }

    # ------------------------------------------------------------------
    # Registration Summary
    # ------------------------------------------------------------------

    def registration_summary(self) -> dict[str, Any]:
        return {
            "datasets": [
                getattr(d, "name", str(type(d)))
                for d in self.datasets
            ],
            "models": [
                getattr(m, "name", m.__class__.__name__)
                for m in self.models
            ],
            "metrics": list(self.metrics.keys()),
        }

    # ------------------------------------------------------------------
    # Timer
    # ------------------------------------------------------------------

    def start_timer(self) -> None:
        self._timer_start = time.perf_counter()

    def stop_timer(self) -> float:
        if self._timer_start is None:
            return 0.0

        elapsed = time.perf_counter() - self._timer_start
        self._timer_start = None
        return elapsed
            # ------------------------------------------------------------------
    # History
    # ------------------------------------------------------------------

    def log_history(self, **kwargs: Any) -> None:
        """Append a history record."""
        self.history.append(dict(kwargs))

    # ------------------------------------------------------------------
    # Results
    # ------------------------------------------------------------------

    def add_result(
        self,
        model: Any,
        dataset: Any,
        metrics: dict[str, Any],
    ) -> None:
        """Store one benchmark result."""

        result = {
            "model": getattr(
                model,
                "name",
                model.__class__.__name__,
            ),
            "dataset": getattr(
                dataset,
                "name",
                dataset.__class__.__name__,
            ),
        }

        result.update(metrics)

        self.results.append(result)

    def results_dataframe(self) -> pd.DataFrame:
        """Return results as a DataFrame."""
        if not self.results:
            return pd.DataFrame()

        return pd.DataFrame(self.results)

    def clear_results(self) -> None:
        """Reset benchmark state."""
        self.results.clear()
        self.history.clear()
        self.statistics = {}

    # ------------------------------------------------------------------
    # Callbacks
    # ------------------------------------------------------------------

    def add_callback(
        self,
        callback: Callable,
    ) -> None:
        self.callbacks.append(callback)

    def _execute_callbacks(
        self,
        event: str,
        **kwargs: Any,
    ) -> None:
        for callback in self.callbacks:
            callback(event, **kwargs)

    # ------------------------------------------------------------------
    # Benchmark Information
    # ------------------------------------------------------------------

    def benchmark_summary(self) -> dict[str, Any]:
        return {
            "benchmark": self.name,
            "models": self.number_of_models,
            "datasets": self.number_of_datasets,
            "metrics": self.number_of_metrics,
            "runs": len(self.results),
            "output_directory": str(self.output_directory),
        }

    def benchmark_metadata(self) -> dict[str, Any]:
        return {
            "system": {
                "platform": platform.system(),
                "python": sys.version,
            },
            "runner": {
                "name": self.name,
                "random_state": self.random_state,
            },
        }

    # ------------------------------------------------------------------
    # Metric Evaluation
    # ------------------------------------------------------------------

    def _evaluate_metrics(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
    ) -> dict[str, float]:

        values: dict[str, float] = {}

        for name, metric in self.metrics.items():

            try:
                values[name] = float(metric(y_true, y_pred))
            except Exception:
                values[name] = float("nan")

        return values

    # ------------------------------------------------------------------
    # Model Execution
    # ------------------------------------------------------------------

    def _fit_model(
        self,
        model: Any,
        X_train: Any,
        y_train: Any,
    ) -> float:

        start = time.perf_counter()

        model.fit(X_train, y_train)

        return time.perf_counter() - start

    def _predict(
        self,
        model: Any,
        X_test: Any,
    ) -> tuple[np.ndarray, float]:

        start = time.perf_counter()

        predictions = model.predict(X_test)

        elapsed = time.perf_counter() - start

        return np.asarray(predictions), elapsed

    # ------------------------------------------------------------------
    # Single Benchmark
    # ------------------------------------------------------------------

    def run_single(
        self,
        model: Any,
        dataset: Any,
    ) -> dict[str, float]:

        self._execute_callbacks("before_run")

        self._fit_model(
            model,
            dataset.X_train,
            dataset.y_train,
        )

        predictions, _ = self._predict(
            model,
            dataset.X_test,
        )

        metrics = self._evaluate_metrics(
            dataset.y_test,
            predictions,
        )

        self.add_result(
            model,
            dataset,
            metrics,
        )

        self.log_history(
            model=getattr(
                model,
                "name",
                model.__class__.__name__,
            ),
            dataset=getattr(
                dataset,
                "name",
                dataset.__class__.__name__,
            ),
            **metrics,
        )

        self._execute_callbacks("after_run")

        return metrics
            # ------------------------------------------------------------------
    # Complete Benchmark
    # ------------------------------------------------------------------

    def run(
        self,
        continue_on_error: bool = False,
    ) -> pd.DataFrame:

        self.validate()

        self._execute_callbacks("benchmark_start")

        for dataset in self.datasets:

            for model in self.models:

                try:
                    self.run_single(
                        model,
                        dataset,
                    )

                except Exception:

                    if not continue_on_error:
                        raise

        self._execute_callbacks("benchmark_end")

        return self.results_dataframe()

    # ------------------------------------------------------------------
    # Cross Validation
    # ------------------------------------------------------------------

    def configure_cross_validation(
        self,
        strategy: str = "kfold",
        folds: int = 5,
    ) -> None:

        self.cv_strategy = strategy
        self.cv_folds = folds

    # ------------------------------------------------------------------
    # Checkpoint
    # ------------------------------------------------------------------

    def save_checkpoint(self) -> None:

        path = self.output_directory / "checkpoint.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "history": self.history,
                },
                f,
                indent=2,
            )

    def load_checkpoint(self) -> None:

        path = self.output_directory / "checkpoint.json"

        if not path.exists():
            return

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.history = data.get("history", [])

    # ------------------------------------------------------------------
    # Resource Profiling
    # ------------------------------------------------------------------

    def profile_system(self) -> dict[str, Any]:

        cpu_count = os.cpu_count() or 1

        try:
            import psutil

            memory = psutil.virtual_memory().total / (1024**3)

        except Exception:
            memory = 0.0

        return {
            "cpu_count": cpu_count,
            "memory_gb": float(memory),
        }

    def memory_usage_mb(self) -> float:

        try:
            import psutil

            process = psutil.Process()

            return float(
                process.memory_info().rss / (1024**2)
            )

        except Exception:
            return 1.0

    def model_size_mb(
        self,
        model: Any,
    ) -> float:

        try:
            size = len(
                pickle.dumps(model)
            ) / (1024**2)

            return float(size)

        except Exception:
            return 0.0

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def export_results(self) -> None:

        self.results_dataframe().to_csv(
            self.output_directory / "results.csv",
            index=False,
        )

    def save_configuration(self) -> None:

        config = {
            "benchmark": self.name,
            "random_state": self.random_state,
            "cv_strategy": self.cv_strategy,
            "cv_folds": self.cv_folds,
        }

        with open(
            self.output_directory / "configuration.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                config,
                f,
                indent=2,
            )

    def export_all(self) -> None:

        self.export_results()
        self.save_configuration()
        self.save_checkpoint()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> None:

        print(self.results_dataframe())

    # ------------------------------------------------------------------
    # Framework Integration
    # ------------------------------------------------------------------

    def attach_leaderboard(
        self,
        leaderboard: Any,
    ) -> None:

        self.leaderboard = leaderboard

    def attach_report(
        self,
        report: Any,
    ) -> None:

        self.report = report

    def attach_experiment(
        self,
        experiment: Any,
    ) -> None:

        self.experiment = experiment

    # ------------------------------------------------------------------
    # Leaderboard
    # ------------------------------------------------------------------

    def update_leaderboard(
        self,
        metric: str,
    ):

        if self.leaderboard is None:
            return None

        if hasattr(self.leaderboard, "update"):
            return self.leaderboard.update(
                self.results_dataframe(),
                metric,
            )

        if hasattr(self.leaderboard, "build"):
            return self.leaderboard.build(
                self.results_dataframe(),
                metric,
            )

        return self.results_dataframe()

    # ------------------------------------------------------------------
    # Report
    # ------------------------------------------------------------------

    def generate_report(self) -> None:

        report_path = (
            self.output_directory
            / "benchmark_report.json"
        )

        data = {
            "summary": self.benchmark_summary(),
            "results": self.results,
        }

        with open(
            report_path,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                data,
                f,
                indent=2,
        )
            
