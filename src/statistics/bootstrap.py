"""
CircuitBench Bootstrap Confidence Intervals
===========================================

Bootstrap confidence intervals for machine learning metrics.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class BootstrapResult:
    estimate: float

    lower: float

    upper: float

    std: float

    samples: np.ndarray


class Bootstrap:
    @staticmethod
    def confidence_interval(
        metric_function,
        y_true,
        y_pred,
        n_bootstrap=1000,
        confidence=0.95,
        random_state=42,
    ):

        rng = np.random.default_rng(random_state)

        y_true = np.asarray(y_true)

        y_pred = np.asarray(y_pred)

        estimate = metric_function(
            y_true,
            y_pred,
        )

        scores = np.zeros(
            n_bootstrap,
            dtype=float,
        )

        n = len(y_true)

        for i in range(n_bootstrap):
            idx = rng.integers(
                0,
                n,
                size=n,
            )

            scores[i] = metric_function(
                y_true[idx],
                y_pred[idx],
            )

        alpha = 1.0 - confidence

        lower = np.percentile(
            scores,
            alpha / 2 * 100,
        )

        upper = np.percentile(
            scores,
            (1 - alpha / 2) * 100,
        )

        return BootstrapResult(
            estimate=float(estimate),
            lower=float(lower),
            upper=float(upper),
            std=float(
                np.std(
                    scores,
                    ddof=1,
                )
            ),
            samples=scores,
        )
