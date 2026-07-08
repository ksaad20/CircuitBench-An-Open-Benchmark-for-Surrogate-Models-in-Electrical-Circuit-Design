"""
Prediction uncertainty metrics.
"""

import numpy as np
from scipy.stats import entropy


def predictive_entropy(probabilities):

    return entropy(probabilities)


def prediction_variance(predictions):

    return np.var(predictions)


def confidence_score(probabilities):

    return np.max(probabilities)


def ensemble_variance(predictions):

    return np.var(
        predictions,
        axis=0
    )


def uncertainty_score(probabilities):

    return 1 - np.max(probabilities)


def coefficient_of_variation(values):

    return np.std(values) / np.mean(values)
