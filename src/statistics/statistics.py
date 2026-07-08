"""
statistics.py
=============

Core statistical utilities for CircuitBench.

Author: Asif Kazi
License: MIT
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from scipy.stats import (
    skew,
    kurtosis,
    sem,
    t,
    zscore,
    iqr,
    entropy,
)


class Statistics:
    """
    General statistical utilities for benchmark analysis.
    """

    @staticmethod
    def count(values):

        return len(values)

    @staticmethod
    def mean(values):

        return float(np.mean(values))

    @staticmethod
    def median(values):

        return float(np.median(values))

    @staticmethod
    def minimum(values):

        return float(np.min(values))

    @staticmethod
    def maximum(values):

        return float(np.max(values))

    @staticmethod
    def variance(values):

        return float(np.var(values, ddof=1))

    @staticmethod
    def standard_deviation(values):

        return float(np.std(values, ddof=1))

    @staticmethod
    def standard_error(values):

        return float(sem(values))

    @staticmethod
    def coefficient_of_variation(values):

        values = np.asarray(values)

        return (
            np.std(values, ddof=1)
            /
            np.mean(values)
        )

    @staticmethod
    def geometric_mean(values):

        values = np.asarray(values)

        return float(
            np.exp(
                np.mean(
                    np.log(values)
                )
            )
        )

    @staticmethod
    def harmonic_mean(values):

        values = np.asarray(values)

        return len(values) / np.sum(
            1.0 / values
        )

    @staticmethod
    def trimmed_mean(values,
                     proportion=0.10):

        values = np.sort(values)

        k = int(len(values) * proportion)

        return np.mean(values[k:-k])

    @staticmethod
    def skewness(values):

        return float(skew(values))

    @staticmethod
    def kurtosis(values):

        return float(kurtosis(values))

    @staticmethod
    def covariance(x,
                   y):

        return np.cov(x, y)[0, 1]

    @staticmethod
    def covariance_matrix(df):

        return df.cov()

    @staticmethod
    def correlation(x,
                    y):

        return np.corrcoef(x, y)[0, 1]

    @staticmethod
    def correlation_matrix(df):

        return df.corr()

    @staticmethod
    def z_scores(values):

        return zscore(values)

    @staticmethod
    def interquartile_range(values):

        return iqr(values)

    @staticmethod
    def median_absolute_deviation(values):

        values = np.asarray(values)

        median = np.median(values)

        return np.median(
            np.abs(values - median)
        )

    @staticmethod
    def detect_outliers(values):

        values = np.asarray(values)

        q1 = np.percentile(values, 25)

        q3 = np.percentile(values, 75)

        iqr_value = q3 - q1

        lower = q1 - 1.5 * iqr_value

        upper = q3 + 1.5 * iqr_value

        return values[
            (values < lower)
            |
            (values > upper)
        ]

    @staticmethod
    def confidence_interval(values,
                            confidence=0.95):

        values = np.asarray(values)

        n = len(values)

        mean = np.mean(values)

        margin = sem(values) * t.ppf(
            (1 + confidence) / 2,
            n - 1
        )

        return {

            "Mean": mean,

            "Lower": mean - margin,

            "Upper": mean + margin,

            "Confidence": confidence

        }

    @staticmethod
    def normalize(values):

        values = np.asarray(values)

        return (

            values -

            np.min(values)

        ) / (

            np.max(values)

            -

            np.min(values)

        )

    @staticmethod
    def entropy(values):

        values = np.asarray(values)

        probabilities = values / np.sum(values)

        return entropy(probabilities)

    @staticmethod
    def weighted_score(metrics,
                       weights):

        score = 0

        for metric in metrics:

            score += (

                metrics[metric]

                *

                weights.get(metric, 1)

            )

        return score

    @staticmethod
    def summary(values):

        return {

            "Count":
            Statistics.count(values),

            "Mean":
            Statistics.mean(values),

            "Median":
            Statistics.median(values),

            "Minimum":
            Statistics.minimum(values),

            "Maximum":
            Statistics.maximum(values),

            "Variance":
            Statistics.variance(values),

            "Std":
            Statistics.standard_deviation(values),

            "StdError":
            Statistics.standard_error(values),

            "CV":
            Statistics.coefficient_of_variation(values),

            "Skewness":
            Statistics.skewness(values),

            "Kurtosis":
            Statistics.kurtosis(values),

            "IQR":
            Statistics.interquartile_range(values),

            "MAD":
            Statistics.median_absolute_deviation(values)

        }

    @staticmethod
    def summary_dataframe(values):

        return pd.DataFrame(

            [Statistics.summary(values)]

        )

    @staticmethod
    def benchmark_summary(results):

        """
        Summarize benchmark results.

        Parameters
        ----------
        results : DataFrame

        Returns
        -------
        DataFrame
        """

        return results.describe()

    @staticmethod
    def model_summary(df,
                      model_name):

        row = df[

            df["Model"] == model_name

        ]

        return row

    @staticmethod
    def compare_models(df,
                       metric="Score"):

        return df.sort_values(

            metric,

            ascending=False

        )

    @staticmethod
    def aggregate_metrics(df):

        return df.mean(
            numeric_only=True
  )
