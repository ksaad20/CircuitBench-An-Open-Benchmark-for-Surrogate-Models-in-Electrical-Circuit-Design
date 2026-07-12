"""
CircuitBench Model Comparison
=============================

Statistical comparison of machine learning models using
paired bootstrap resampling.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class ComparisonResult:
    model_a_score: float

    model_b_score: float

    difference: float

    ci_lower: float

    ci_upper: float

    p_value: float

    bootstrap_differences: np.ndarray


class ModelComparison:
    @staticmethod
    def paired_bootstrap(
        metric_function,
        y_true,
        pred_a,
        pred_b,
        n_bootstrap=2000,
        confidence=0.95,
        random_state=42,
    ):

        rng = np.random.default_rng(random_state)

        y_true = np.asarray(y_true)

        pred_a = np.asarray(pred_a)

        pred_b = np.asarray(pred_b)

        n = len(y_true)

        score_a = metric_function(
            y_true,
            pred_a,
        )

        score_b = metric_function(
            y_true,
            pred_b,
        )

        diffs = np.zeros(
            n_bootstrap,
            dtype=float,
        )

        for i in range(n_bootstrap):
            idx = rng.integers(
                0,
                n,
                size=n,
            )

            a = metric_function(
                y_true[idx],
                pred_a[idx],
            )

            b = metric_function(
                y_true[idx],
                pred_b[idx],
            )

            diffs[i] = a - b

        alpha = 1.0 - confidence

        lower = np.percentile(
            diffs,
            alpha / 2 * 100,
        )

        upper = np.percentile(
            diffs,
            (1 - alpha / 2) * 100,
        )

        p = 2 * min(
            np.mean(diffs <= 0),
            np.mean(diffs >= 0),
        )

        return ComparisonResult(
            model_a_score=float(score_a),
            model_b_score=float(score_b),
            difference=float(score_a - score_b),
            ci_lower=float(lower),
            ci_upper=float(upper),
            p_value=float(p),
            bootstrap_differences=diffs,
        )
