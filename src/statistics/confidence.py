"""
Confidence Interval Utilities
"""

from __future__ import annotations

import numpy as np

from scipy.stats import sem
from scipy.stats import t


class ConfidenceInterval:

    @staticmethod
    def mean(values, confidence=0.95):
        """
        Confidence interval of the mean.
        """

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

    @staticmethod
    def width(values, confidence=0.95):

        ci = ConfidenceInterval.mean(
            values,
            confidence
        )

        return ci["upper"] - ci["lower"]
