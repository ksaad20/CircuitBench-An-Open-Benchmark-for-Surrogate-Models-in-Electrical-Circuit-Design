"""
Visualization tests.
"""

import matplotlib.pyplot as plt


def test_plot_creation():

    fig = plt.figure()

    plt.plot([1, 2, 3], [2, 4, 6])

    assert len(fig.axes) == 1

    plt.close(fig)
