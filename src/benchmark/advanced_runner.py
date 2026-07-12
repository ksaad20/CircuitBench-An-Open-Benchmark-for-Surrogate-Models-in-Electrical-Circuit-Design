"""
CircuitBench Advanced Benchmark Runner
======================================

Advanced benchmark execution engine.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
import tracemalloc

import numpy as np
import pandas as pd

from sklearn.base import clone
from sklearn.model_selection import cross_validate


@dataclass
class AdvancedBenchmarkResult:
    model_name: str

    task: str

    fit_time: float

    predict_time: float

    memory_mb: float

    metrics: dict


class AdvancedBenchmarkRunner:
    def __init__(
        self,
        metrics,
    ):

        self.metrics = metrics

    @staticmethod
    def detect_task(
        y,
    ):

        y = np.asarray(y)

        unique = np.unique(y)

        if y.dtype.kind in "ifu":
            if len(unique) <= 20:
                return "classification"

        return "regression"

    def evaluate(
        self,
        model,
        X_train,
        y_train,
        X_test,
        y_test,
    ):

        tracemalloc.start()

        start = perf_counter()

        model.fit(
            X_train,
            y_train,
        )

        fit_time = perf_counter() - start

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        start = perf_counter()

        predictions = model.predict(X_test)

        predict_time = perf_counter() - start

        task = self.detect_task(y_train)

        results = {}

        for name, metric in self.metrics.items():
            try:
                results[name] = metric(
                    y_test,
                    predictions,
                )

            except Exception:
                results[name] = np.nan

        return AdvancedBenchmarkResult(
            model_name=model.__class__.__name__,
            task=task,
            fit_time=float(fit_time),
            predict_time=float(predict_time),
            memory_mb=float(peak / 1024 / 1024),
            metrics=results,
        )

    def cross_validate(
        self,
        model,
        X,
        y,
        cv=5,
        scoring=None,
    ):

        estimator = clone(model)

        return cross_validate(
            estimator,
            X,
            y,
            cv=cv,
            scoring=scoring,
            return_train_score=True,
        )

    @staticmethod
    def results_dataframe(
        results,
    ):

        rows = []

        for r in results:
            row = {
                "Model": r.model_name,
                "Task": r.task,
                "FitTime": r.fit_time,
                "PredictTime": r.predict_time,
                "MemoryMB": r.memory_mb,
            }

            row.update(r.metrics)

            rows.append(row)

        return pd.DataFrame(rows)
