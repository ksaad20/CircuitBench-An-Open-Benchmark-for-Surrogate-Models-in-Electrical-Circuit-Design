"""
Fairness metrics.
"""

import numpy as np


def demographic_parity(group_a, group_b):

    return abs(
        np.mean(group_a)
        -
        np.mean(group_b)
    )


def equal_opportunity(tpr_a, tpr_b):

    return abs(tpr_a - tpr_b)


def disparate_impact(rate_a, rate_b):

    return rate_a / rate_b


def fairness_score(group_a, group_b):

    return 1 - demographic_parity(
        group_a,
        group_b
    )
