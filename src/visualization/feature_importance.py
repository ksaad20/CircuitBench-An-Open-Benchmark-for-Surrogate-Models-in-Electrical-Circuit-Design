"""
Feature importance visualization.
"""

import matplotlib.pyplot as plt


def importance(features, scores):

    plt.barh(features, scores)

    plt.xlabel("Importance")

    plt.tight_layout()

    plt.show()
