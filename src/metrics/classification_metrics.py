"""
CircuitBench Classification Metrics
==================================

Comprehensive classification metrics for benchmarking.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    cohen_kappa_score,
    confusion_matrix,
)


class ClassificationMetrics:
    """
    Collection of classification evaluation metrics.
    """

    @staticmethod
    def accuracy(
        y_true,
        y_pred,
    ) -> float:

        return float(
            accuracy_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def balanced_accuracy(
        y_true,
        y_pred,
    ) -> float:

        return float(
            balanced_accuracy_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def precision(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            precision_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def recall(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            recall_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def f1(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            f1_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def matthews_cc(
        y_true,
        y_pred,
    ) -> float:

        return float(
            matthews_corrcoef(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def cohen_kappa(
        y_true,
        y_pred,
    ) -> float:

        return float(
            cohen_kappa_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def confusion(
        y_true,
        y_pred,
    ) -> np.ndarray:

        return confusion_matrix(
            y_true,
            y_pred,
        )

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_pred,
    ) -> dict[str, Any]:

        return {
            "Accuracy": cls.accuracy(
                y_true,
                y_pred,
            ),
            "BalancedAccuracy": cls.balanced_accuracy(
                y_true,
                y_pred,
            ),
            "Precision": cls.precision(
                y_true,
                y_pred,
            ),
            "Recall": cls.recall(
                y_true,
                y_pred,
            ),
            "F1": cls.f1(
                y_true,
                y_pred,
            ),
            "MatthewsCC": cls.matthews_cc(
                y_true,
                y_pred,
            ),
            "CohenKappa": cls.cohen_kappa(
                y_true,
                y_pred,
            ),
        }


from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    log_loss,
    brier_score_loss,
    top_k_accuracy_score,
    roc_curve,
    precision_recall_curve,
)


    @staticmethod
    def roc_auc(
        y_true,
        y_score,
        multi_class="ovr",
    ) -> float:
        """
        Receiver Operating Characteristic Area Under Curve.
        """

        return float(
            roc_auc_score(
                y_true,
                y_score,
                multi_class=multi_class,
            )
        )

    @staticmethod
    def pr_auc(
        y_true,
        y_score,
    ) -> float:
        """
        Precision-Recall Area Under Curve.
        """

        return float(
            average_precision_score(
                y_true,
                y_score,
            )
        )

    @staticmethod
    def logarithmic_loss(
        y_true,
        y_prob,
    ) -> float:
        """
        Cross-entropy / Log Loss.
        """

        return float(
            log_loss(
                y_true,
                y_prob,
            )
        )

    @staticmethod
    def brier_score(
        y_true,
        y_prob,
    ) -> float:
        """
        Brier Score.
        """

        return float(
            brier_score_loss(
                y_true,
                y_prob,
            )
        )

    @staticmethod
    def top_k_accuracy(
        y_true,
        y_score,
        k=2,
    ) -> float:
        """
        Top-K Accuracy.
        """

        return float(
            top_k_accuracy_score(
                y_true,
                y_score,
                k=k,
            )
        )

    @staticmethod
    def roc_curve_data(
        y_true,
        y_score,
    ):
        """
        Return FPR, TPR and thresholds for plotting ROC curves.
        """

        return roc_curve(
            y_true,
            y_score,
        )

    @staticmethod
    def precision_recall_curve_data(
        y_true,
        y_score,
    ):
        """
        Return precision, recall and thresholds for plotting PR curves.
        """

        return precision_recall_curve(
            y_true,
            y_score,
        )

