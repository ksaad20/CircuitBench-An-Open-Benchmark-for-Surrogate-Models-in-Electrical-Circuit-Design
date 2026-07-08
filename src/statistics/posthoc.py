"""
posthoc.py
==========

Post-hoc statistical tests for CircuitBench.

Author: Asif Kazi
License: MIT
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from scipy.stats import rankdata
from scipy.stats import wilcoxon

try:
    import scikit_posthocs as sp
    HAS_POSTHOC = True
except ImportError:
    HAS_POSTHOC = False


class PostHoc:
    """
    Post-hoc statistical analysis.
    """

    @staticmethod
    def nemenyi(data):
        """
        Nemenyi post-hoc test.

        Parameters
        ----------
        data : array-like
            Matrix of shape (datasets, models)

        Returns
        -------
        DataFrame
        """

        if not HAS_POSTHOC:
            raise ImportError(
                "Install scikit-posthocs first."
            )

        return sp.posthoc_nemenyi_friedman(data)

    @staticmethod
    def dunn(data,
             p_adjust="holm"):

        if not HAS_POSTHOC:
            raise ImportError(
                "Install scikit-posthocs first."
            )

        return sp.posthoc_dunn(
            data,
            p_adjust=p_adjust
        )

    @staticmethod
    def pairwise_wilcoxon(df):

        models = list(df.columns)

        results = []

        for i in range(len(models)):

            for j in range(i + 1,
                           len(models)):

                statistic, p = wilcoxon(
                    df[models[i]],
                    df[models[j]]
                )

                results.append({

                    "Model A":
                    models[i],

                    "Model B":
                    models[j],

                    "Statistic":
                    statistic,

                    "p-value":
                    p

                })

        return pd.DataFrame(results)

    @staticmethod
    def average_ranks(df):

        ranks = df.rank(
            axis=1,
            ascending=False
        )

        return ranks.mean()
