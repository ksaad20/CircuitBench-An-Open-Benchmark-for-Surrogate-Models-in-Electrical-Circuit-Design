"""
CircuitBench Ranking Metrics
============================

Ranking and retrieval metrics.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np


class RankingMetrics:
    """
    Ranking evaluation metrics.
    """

    @staticmethod
    def precision_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Precision@K
        """

        y_true = np.asarray(y_true)[:k]
        y_pred = np.asarray(y_pred)[:k]

        return float(
            np.sum(y_true == y_pred)
            / k
        )

    @staticmethod
    def recall_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Recall@K
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred[:k])

        relevant = np.isin(
            y_pred,
            y_true,
        )

        if len(y_true) == 0:
            return 0.0

        return float(
            np.sum(relevant)
            / len(y_true)
        )

    @staticmethod
    def hit_rate(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Hit@K
        """

        y_true = set(y_true)

        y_pred = set(y_pred[:k])

        return float(
            len(
                y_true.intersection(
                    y_pred
                )
            ) > 0
        )

    @staticmethod
    def reciprocal_rank(
        y_true,
        y_pred,
    ):
        """
        Reciprocal Rank
        """

        for rank, item in enumerate(
            y_pred,
            start=1,
        ):

            if item in y_true:

                return 1.0 / rank

        return 0.0

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_pred,
        k=10,
    ):

        return {

            "Precision@K":
                cls.precision_at_k(
                    y_true,
                    y_pred,
                    k,
                ),

            "Recall@K":
                cls.recall_at_k(
                    y_true,
                    y_pred,
                    k,
                ),

            "HitRate":
                cls.hit_rate(
                    y_true,
                    y_pred,
                    k,
                ),

            "ReciprocalRank":
                cls.reciprocal_rank(
                    y_true,
                    y_pred,
                ),

        }


__all__ = [
    "RankingMetrics",
]
