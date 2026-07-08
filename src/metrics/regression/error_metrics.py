"""
Regression evaluation metrics for CircuitBench.
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    mean_absolute_error as sk_mae,
    mean_squared_error as sk_mse,
    median_absolute_error as sk_median_ae,
    max_error as sk_max_error,
    mean_squared_log_error
)

def mean_absolute_error(
        y_true,
        y_pred):
    """
    Compute Mean Absolute Error (MAE).

    Parameters
    ----------
    y_true : array-like
        Ground truth values.

    y_pred : array-like
        Predicted values.

    Returns
    -------
    float
        Mean absolute error.
    """

    return float(
        sk_mae(
            y_true,
            y_pred
        )
    )


def mean_squared_error(
        y_true,
        y_pred):
    """
    Compute Mean Squared Error (MSE).
    """

    return float(
        sk_mse(
            y_true,
            y_pred
        )
    )


def root_mean_squared_error(
        y_true,
        y_pred):
    """
    Compute Root Mean Squared Error (RMSE).
    """

    mse = sk_mse(
        y_true,
        y_pred
    )

    return float(
        np.sqrt(mse)
    )



def root_mean_squared_log_error(
        y_true,
        y_pred):
    """
    Compute Root Mean Squared Logarithmic Error (RMSLE).

    Negative values are clipped to zero.
    """

    y_true = np.clip(
        np.asarray(y_true),
        0,
        None
    )

    y_pred = np.clip(
        np.asarray(y_pred),
        0,
        None
    )

    msle = mean_squared_log_error(
        y_true,
        y_pred
    )

    return float(
        np.sqrt(msle)
    )

def median_absolute_error(
        y_true,
        y_pred):
    """
    Compute Median Absolute Error.
    """

    return float(
        sk_median_ae(
            y_true,
            y_pred
        )
    )

def max_error(
        y_true,
        y_pred):
    """
    Compute Maximum Residual Error.
    """

    return float(
        sk_max_error(
            y_true,
            y_pred
        )
    )

def mean_bias_error(
        y_true,
        y_pred):
    """
    Compute Mean Bias Error (MBE).

    Positive values indicate
    overestimation.

    Negative values indicate
    underestimation.
    """

    y_true = np.asarray(
        y_true
    )

    y_pred = np.asarray(
        y_pred
    )

    return float(

        np.mean(

            y_pred - y_true

        )

    )

def mean_percentage_error(
        y_true,
        y_pred):
    """
    Mean Percentage Error (MPE).
    """

    y_true = np.asarray(
        y_true
    )

    y_pred = np.asarray(
        y_pred
    )

    mask = y_true != 0

    return float(

        np.mean(

            (

                y_pred[mask]

                -

                y_true[mask]

            )

            /

            y_true[mask]

        )

        * 100

    )

def mean_absolute_percentage_error(
        y_true,
        y_pred):
    """
    Mean Absolute Percentage Error (MAPE).
    """

    y_true = np.asarray(
        y_true
    )

    y_pred = np.asarray(
        y_pred
    )

    mask = y_true != 0

    return float(

        np.mean(

            np.abs(

                (

                    y_true[mask]

                    -

                    y_pred[mask]

                )

                /

                y_true[mask]

            )

        )

        * 100

          )

def symmetric_mean_absolute_percentage_error(
        y_true,
        y_pred):
    """
    Symmetric Mean Absolute
    Percentage Error (SMAPE).
    """

    y_true = np.asarray(
        y_true
    )

    y_pred = np.asarray(
        y_pred
    )

    denominator = (

        np.abs(y_true)

        +

        np.abs(y_pred)

    ) / 2

    mask = denominator != 0

    return float(

        np.mean(

            np.abs(

                y_true[mask]

                -

                y_pred[mask]

            )

            /

            denominator[mask]

        )

        * 100

    )

