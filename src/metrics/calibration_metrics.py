"""
CircuitBench Calibration Metrics
================================

Calibration metrics for probabilistic machine learning models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np

from sklearn.calibration import calibration_curve


class CalibrationMetrics:
    """
    Calibration metrics.
    """

    @staticmethod
    def expected_calibration_error(
        y_true,
        y_prob,
        n_bins=10,
    ):
        """
        Expected Calibration Error (ECE).
        """

        y_true = np.asarray(y_true)
        y_prob = np.asarray(y_prob)

        bins = np.linspace(
            0.0,
            1.0,
            n_bins + 1,
        )

        ece = 0.0

        for i in range(n_bins):

            mask = (

                (y_prob >= bins[i])

                &

                (y_prob < bins[i + 1])

            )

            if np.any(mask):

                accuracy = np.mean(
                    y_true[mask]
                )

                confidence = np.mean(
                    y_prob[mask]
                )

                ece += (

                    np.sum(mask)

                    /

                    len(y_true)

                ) * abs(

                    accuracy

                    -

                    confidence

                )

        return float(ece)

    @staticmethod
    def calibration_curve_data(
        y_true,
        y_prob,
        n_bins=10,
    ):
        """
        Returns calibration curve data.
        """

        return calibration_curve(

            y_true,

            y_prob,

            n_bins=n_bins,

        )

