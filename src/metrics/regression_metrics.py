"""
CircuitBench Regression Metrics
===============================

Regression metrics used throughout CircuitBench.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    median_absolute_error,
    max_error,
    explained_variance_score,
    r2_score,
)


class RegressionMetrics:
    """
    Collection of regression evaluation metrics.
    """

    @staticmethod
    def mae(y_true, y_pred):

        return float(

            mean_absolute_error(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def mse(y_true, y_pred):

        return float(

            mean_squared_error(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def rmse(y_true, y_pred):

        return float(

            np.sqrt(

                mean_squared_error(

                    y_true,

                    y_pred,

                )

            )

        )

    @staticmethod
    def median_absolute_error(

        y_true,

        y_pred,

    ):

        return float(

            median_absolute_error(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def max_error(

        y_true,

        y_pred,

    ):

        return float(

            max_error(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def explained_variance(

        y_true,

        y_pred,

    ):

        return float(

            explained_variance_score(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def r2(

        y_true,

        y_pred,

    ):

        return float(

            r2_score(

                y_true,

                y_pred,

            )

        )

    @staticmethod
    def adjusted_r2(

        y_true,

        y_pred,

        n_features,

    ):

        n = len(y_true)

        r2 = RegressionMetrics.r2(

            y_true,

            y_pred,

        )

        return float(

            1

            -

            (

                (1-r2)

                *

                (n-1)

                /

                (n-n_features-1)

            )

        )

    @staticmethod
    def mape(

        y_true,

        y_pred,

    ):

        y_true = np.asarray(

            y_true,

            dtype=float,

        )

        y_pred = np.asarray(

            y_pred,

            dtype=float,

        )

        epsilon = np.finfo(float).eps

        return float(

            np.mean(

                np.abs(

                    (y_true-y_pred)

                    /

                    np.maximum(

                        np.abs(y_true),

                        epsilon,

                    )

                )

            )

            *100

        )

    @classmethod
    def all_metrics(

        cls,

        y_true,

        y_pred,

        n_features=1,

    ):

        return {

            "MAE":

                cls.mae(

                    y_true,

                    y_pred,

                ),

            "MSE":

                cls.mse(

                    y_true,

                    y_pred,

                ),

            "RMSE":

                cls.rmse(

                    y_true,

                    y_pred,

                ),

            "MedianAE":

                cls.median_absolute_error(

                    y_true,

                    y_pred,

                ),

            "MAPE":

                cls.mape(

                    y_true,

                    y_pred,

                ),

            "R2":

                cls.r2(

                    y_true,

                    y_pred,

                ),

            "Adjusted_R2":

                cls.adjusted_r2(

                    y_true,

                    y_pred,

                    n_features,

                ),

            "ExplainedVariance":

                cls.explained_variance(

                    y_true,

                    y_pred,

                ),

            "MaxError":

                cls.max_error(

                    y_true,

                    y_pred,

                ),

        }


__all__ = [

    "RegressionMetrics",

]

