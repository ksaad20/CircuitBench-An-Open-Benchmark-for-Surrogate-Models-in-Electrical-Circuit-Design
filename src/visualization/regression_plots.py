"""
CircuitBench Regression Visualization
====================================

Publication-quality regression visualizations.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


class RegressionPlots:
    """
    Regression visualization utilities.
    """

    @staticmethod
    def plot_actual_vs_predicted(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Scatter plot of actual vs predicted values.
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.scatter(
            y_true,
            y_pred,
            alpha=0.7,
        )

        minimum = min(
            np.min(y_true),
            np.min(y_pred),
        )

        maximum = max(
            np.max(y_true),
            np.max(y_pred),
        )

        ax.plot(
            [minimum, maximum],
            [minimum, maximum],
            linestyle="--",
            linewidth=2,
        )

        ax.set_xlabel("Actual")

        ax.set_ylabel("Predicted")

        ax.set_title(
            "Actual vs Predicted"
        )

        return ax

    @staticmethod
    def plot_residuals(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Residual plot.
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        residuals = y_true - y_pred

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.scatter(
            y_pred,
            residuals,
            alpha=0.7,
        )

        ax.axhline(
            0,
            linestyle="--",
        )

        ax.set_xlabel(
            "Predicted"
        )

        ax.set_ylabel(
            "Residual"
        )

        ax.set_title(
            "Residual Plot"
        )

        return ax

    @staticmethod
    def plot_error_distribution(
        y_true,
        y_pred,
        bins=30,
        ax=None,
    ):
        """
        Histogram of prediction errors.
        """

        errors = np.asarray(y_true) - np.asarray(y_pred)

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.hist(
            errors,
            bins=bins,
        )

        ax.set_xlabel(
            "Prediction Error"
        )

        ax.set_ylabel(
            "Frequency"
        )

        ax.set_title(
            "Prediction Error Distribution"
        )

        return ax


__all__ = [
    "RegressionPlots",
]

