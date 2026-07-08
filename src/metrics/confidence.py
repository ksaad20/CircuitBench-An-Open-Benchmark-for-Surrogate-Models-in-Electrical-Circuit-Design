"""
Confidence metrics.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import sem, t


def confidence_interval(values, confidence=0.95):

    values = np.asarray(values)

    n = len(values)

    mean = np.mean(values)

    margin = sem(values) * t.ppf(
        (1 + confidence) / 2,
        n - 1
    )

    return {
        "mean": mean,
        "lower": mean - margin,
        "upper": mean + margin,
        "confidence": confidence
    }


def interval_width(values, confidence=0.95):

    ci = confidence_interval(values, confidence)

    return ci["upper"] - ci["lower"]


def confidence_score(values):

    width = interval_width(values)

    return 1 / (1 + width)
