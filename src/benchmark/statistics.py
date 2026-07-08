"""
statistics.py
=============

Statistical analysis utilities for CircuitBench.

Author: Asif Kazi
License: Apache 2.0
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from scipy.stats import (
    ttest_rel,
    ttest_ind,
    wilcoxon,
    friedmanchisquare,
    shapiro,
    sem,
    t,
)


class Statistics:
    """
    Statistical analysis utilities.
    """

    @staticmethod
    def mean(values):
        return float(np.mean(values))

    @staticmethod
    def median(values):
        return float(np.median(values))

    @staticmethod
    def variance(values):
        return float(np.var(values, ddof=1))

    @staticmethod
    def std(values):
        return float(np.std(values, ddof=1))

    @staticmethod
    def minimum(values):
        return float(np.min(values))

    @staticmethod
    def maximum(values):
        return float(np.max(values))

    @staticmethod
    def summary(values):
        """
        Return descriptive statistics.
        """

        values = np.asarray(values)

        return {
            "Count": len(values),
            "Mean": Statistics.mean(values),
            "Median": Statistics.median(values),
            "Std": Statistics.std(values),
            "Variance": Statistics.variance(values),
            "Minimum": Statistics.minimum(values),
            "Maximum": Statistics.maximum(values),
        }

    @staticmethod
    def confidence_interval(values, confidence=0.95):
        """
        Compute confidence interval of the mean.
        """

        values = np.asarray(values)

        n = len(values)

        mean = np.mean(values)

        margin = sem(values) * t.ppf(
            (1 + confidence) / 2.0,
            n - 1
        )

        return (
            mean - margin,
            mean + margin
        )

    @staticmethod
    def shapiro_test(values):
        """
        Shapiro-Wilk normality test.
        """

        statistic, p = shapiro(values)

        return {
            "Statistic": statistic,
            "p-value": p
        }

    @staticmethod
    def paired_t_test(a, b):
        """
        Paired Student t-test.
        """

        statistic, p = ttest_rel(a, b)

        return {
            "Statistic": statistic,
            "p-value": p
        }

    @staticmethod
    def independent_t_test(a, b):
        """
        Independent Student t-test.
        """

        statistic, p = ttest_ind(
            a,
            b,
            equal_var=False
        )

        return {
            "Statistic": statistic,
            "p-value": p
        }

    @staticmethod
    def wilcoxon_test(a, b):
        """
        Wilcoxon signed-rank test.
        """

        statistic, p = wilcoxon(a, b)

        return {
            "Statistic": statistic,
            "p-value": p
        }

    @staticmethod
    def friedman_test(*groups):
        """
        Friedman test for comparing multiple models.
        """

        statistic, p = friedmanchisquare(*groups)

        return {
            "Statistic": statistic,
            "p-value": p
        }

    @staticmethod
    def cohens_d(a, b):
        """
        Cohen's d effect size.
        """

        a = np.asarray(a)
        b = np.asarray(b)

        pooled_std = np.sqrt(
            (
                ((len(a) - 1) * np.var(a, ddof=1))
                +
                ((len(b) - 1) * np.var(b, ddof=1))
            )
            /
            (len(a) + len(b) - 2)
        )

        return (
            np.mean(a) - np.mean(b)
        ) / pooled_std

    @staticmethod
    def correlation(x, y):
        """
        Pearson correlation.
        """

        return np.corrcoef(x, y)[0, 1]

    @staticmethod
    def dataframe(values):
        """
        Convert statistics to DataFrame.
        """

        return pd.DataFrame(
            [Statistics.summary(values)]
                     )
