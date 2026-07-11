"""
CircuitBench Benchmark Runner
=============================

Central engine responsible for training, evaluating and comparing
all registered models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import time
from typing import Any, Dict, List

import numpy as np

from src.models.factory import ModelFactory


class BenchmarkRunner:
    """
    Central benchmark engine.
    """

    def __init__(self):

        self.results = []

    # -------------------------------------------------------

    def evaluate_model(
        self,
        model,
        X_train,
        y_train,
        X_test,
        y_test,
    ) -> Dict[str, Any]:

        start = time.perf_counter()

        model.fit(X_train, y_train)

        train_time = time.perf_counter() - start

        start = time.perf_counter()

        predictions = model.predict(X_test)

        inference_time = time.perf_counter() - start

        score = model.score(
            X_test,
            y_test,
        )

        result = {

            "model": model.name,

            "score": float(score),

            "train_time": train_time,

            "inference_time": inference_time,

            "n_train": len(y_train),

            "n_test": len(y_test),

        }

        self.results.append(result)

        return result

    # -------------------------------------------------------

    def evaluate_models(

        self,

        model_names: List[str],

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        results = []

        for name in model_names:

            model = ModelFactory.create(name)

            results.append(

                self.evaluate_model(

                    model,

                    X_train,

                    y_train,

                    X_test,

                    y_test,

                )

            )

        return results

    # -------------------------------------------------------

    def leaderboard(self):

        return sorted(

            self.results,

            key=lambda x: x["score"],

            reverse=True,

        )

    # -------------------------------------------------------

    def clear(self):

        self.results.clear()

    # -------------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Benchmark Summary")

        print("=" * 70)

        for row in self.leaderboard():

            print(

                f"{row['model']:25}"

                f"{row['score']:.4f}"

            )

        print("=" * 70)

