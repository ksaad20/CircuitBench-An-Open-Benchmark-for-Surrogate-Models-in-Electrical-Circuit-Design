"""
Calibration metrics.
"""

import numpy as np


def expected_calibration_error(
        confidence,
        accuracy):

    confidence = np.asarray(confidence)

    accuracy = np.asarray(accuracy)

    return np.mean(
        np.abs(
            confidence
            -
            accuracy
        )
    )


def maximum_calibration_error(
        confidence,
        accuracy):

    confidence = np.asarray(confidence)

    accuracy = np.asarray(accuracy)

    return np.max(
        np.abs(
            confidence
            -
            accuracy
        )
    )


def calibration_score(
        confidence,
        accuracy):

    return 1 - expected_calibration_error(
        confidence,
        accuracy
    )
