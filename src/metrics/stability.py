"""
CircuitBench Stability Metrics
==============================

Functions for evaluating the stability and consistency of surrogate models.

Author: CircuitBench
License: Apache 2.0
"""

from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np


def metric_variance(values: Sequence[float]) -> float:
    """
    Compute variance of repeated metric values.

    Parameters
    ----------
    values : Sequence[float]

    Returns
    -------
    float
        Population variance.
    """
    x = np.asarray(values, dtype=float)

    if x.size < 2:
        raise ValueError("At least two observations are required.")

    return float(np.var(x))


def metric_std(values: Sequence[float]) -> float:
    """
    Standard deviation of repeated evaluations.
    """
    x = np.asarray(values, dtype=float)

    if x.size < 2:
        raise ValueError("At least two observations are required.")

    return float(np.std(x))


def coefficient_of_variation(values: Sequence[float]) -> float:
    """
    Relative standard deviation.

    Returns
    -------
    float
        std / mean
    """
    x = np.asarray(values, dtype=float)

    mean = np.mean(x)

    if np.isclose(mean, 0.0):
        raise ZeroDivisionError("Mean is zero.")

    return float(np.std(x) / mean)


def repeatability_score(values: Sequence[float]) -> float:
    """
    Repeatability score between 0 and 1.

    1 indicates perfectly repeatable.
    """

    cv = coefficient_of_variation(values)

    return float(1.0 / (1.0 + cv))


def consistency_score(values: Sequence[float]) -> float:
    """
    Consistency score based on normalized variance.

    Higher is better.
    """

    x = np.asarray(values, dtype=float)

    variance = np.var(x)

    return float(np.exp(-variance))


def stability_index(values: Sequence[float]) -> float:
    """
    Composite stability metric.

    Combines repeatability and consistency.

    Returns
    -------
    float
        Stability index between 0 and 1.
    """

    r = repeatability_score(values)
    c = consistency_score(values)

    return float((r + c) / 2.0)


def performance_drift(
    reference: Sequence[float],
    comparison: Sequence[float],
) -> float:
    """
    Compute average performance drift.

    Positive values indicate degradation.
    """

    ref = np.asarray(reference, dtype=float)
    cmp = np.asarray(comparison, dtype=float)

    if ref.shape != cmp.shape:
        raise ValueError("Arrays must have identical shape.")

    return float(np.mean(cmp - ref))


def seed_stability(results: Iterable[Sequence[float]]) -> float:
    """
    Stability across multiple random seeds.

    Parameters
    ----------
    results :
        List of metric vectors.

    Returns
    -------
    float
        Mean stability index.
    """

    scores = []

    for r in results:
        scores.append(stability_index(r))

    return float(np.mean(scores))


def cross_validation_stability(
    fold_scores: Sequence[float],
) -> float:
    """
    Stability across cross-validation folds.
    """

    return stability_index(fold_scores)


def confidence_band(values: Sequence[float]) -> tuple[float, float]:
    """
    Approximate 95% confidence band.

    Returns
    -------
    (lower, upper)
    """

    x = np.asarray(values, dtype=float)

    mean = np.mean(x)
    std = np.std(x)

    margin = 1.96 * std

    return (
        float(mean - margin),
        float(mean + margin),
    )


def summary(values: Sequence[float]) -> dict:
    """
    Complete stability summary.

    Returns
    -------
    dict
    """

    return {
        "mean": float(np.mean(values)),
        "variance": metric_variance(values),
        "std": metric_std(values),
        "cv": coefficient_of_variation(values),
        "repeatability": repeatability_score(values),
        "consistency": consistency_score(values),
        "stability_index": stability_index(values),
        "confidence_band": confidence_band(values),
      }
