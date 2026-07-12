"""
CircuitBench Figure Generator
=============================

Automatic publication-quality figures.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class FigureGenerator:

    @staticmethod
    def metric_barplot(
        leaderboard,
        metric,
        output=None,
        figsize=(8, 5),
    ):

        df = leaderboard.sort_values(
            metric,
            ascending=False,
        )

        fig, ax = plt.subplots(figsize=figsize)

        ax.bar(
            df["Model"],
            df[metric],
        )

        ax.set_ylabel(metric)

        ax.set_xlabel("Model")

        ax.set_title(f"{metric} Comparison")

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.tight_layout()

        if output:

            Path(output).parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            plt.savefig(
                output,
                dpi=300,
                bbox_inches="tight",
            )

        return fig, ax

    @staticmethod
    def fit_time_plot(
        leaderboard,
        output=None,
    ):

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            leaderboard["Model"],
            leaderboard["FitTime"],
        )

        ax.set_ylabel("Seconds")

        ax.set_title("Model Training Time")

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.tight_layout()

        if output:

            plt.savefig(
                output,
                dpi=300,
                bbox_inches="tight",
            )

        return fig, ax

    @staticmethod
    def prediction_time_plot(
        leaderboard,
        output=None,
    ):

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            leaderboard["Model"],
            leaderboard["PredictTime"],
        )

        ax.set_ylabel("Seconds")

        ax.set_title("Prediction Time")

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.tight_layout()

        if output:

            plt.savefig(
                output,
                dpi=300,
                bbox_inches="tight",
            )

        return fig, ax

    @staticmethod
    def memory_plot(
        leaderboard,
        output=None,
    ):

        if "MemoryMB" not in leaderboard.columns:

            return None

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.bar(
            leaderboard["Model"],
            leaderboard["MemoryMB"],
        )

        ax.set_ylabel("MB")

        ax.set_title("Peak Memory Usage")

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.tight_layout()

        if output:

            plt.savefig(
                output,
                dpi=300,
                bbox_inches="tight",
            )

        return fig, ax
