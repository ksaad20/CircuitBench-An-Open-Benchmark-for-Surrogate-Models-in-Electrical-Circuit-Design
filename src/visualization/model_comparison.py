"""
Compare multiple ML models.
"""

import matplotlib.pyplot as plt


def compare_r2(names, scores):

    plt.bar(names, scores)

    plt.ylabel("R²")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


def compare_rmse(names, errors):

    plt.bar(names, errors)

    plt.ylabel("RMSE")

    plt.tight_layout()

    plt.show()
