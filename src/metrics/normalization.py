"""
Normalization utilities.
"""

import numpy as np


def minmax(values):
    x = np.asarray(values, dtype=float)
    return (x - x.min()) / (x.max() - x.min())


def zscore(values):
    x = np.asarray(values, dtype=float)
    return (x - x.mean()) / x.std()


def robust_scale(values):
    x = np.asarray(values, dtype=float)
    med = np.median(x)
    iqr = np.percentile(x, 75) - np.percentile(x, 25)
    return (x - med) / iqr


def normalize_scores(values, method="minmax"):
    if method == "minmax":
        return minmax(values)
    if method == "zscore":
        return zscore(values)
    if method == "robust":
        return robust_scale(values)
    raise ValueError("Unknown normalization method.")
