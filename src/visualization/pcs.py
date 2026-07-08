"""
PCA visualization.
"""

import matplotlib.pyplot as plt


def plot_pca(x, y, labels=None):

    plt.scatter(x, y)

    if labels:

        for i, label in enumerate(labels):

            plt.text(x[i], y[i], label)

    plt.xlabel("PC1")

    plt.ylabel("PC2")

    plt.show()
