"""
ranking.py
==========

Ranking utilities.

Author: Asif Kazi
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class Ranking:

    def __init__(self):

        self.results = pd.DataFrame()

    def load(self,
             dataframe):

        self.results = dataframe.copy()

    def sort(self,
             metric="Score",
             ascending=False):

        return self.results.sort_values(
            metric,
            ascending=ascending
        )

    def rank(self,
             metric="Score",
             ascending=False):

        df = self.sort(
            metric,
            ascending
        )

        df["Rank"] = np.arange(
            1,
            len(df)+1
        )

        cols = ["Rank"] + [
            c for c in df.columns
            if c != "Rank"
        ]

        return df[cols]

    def top(self,
            n=5):

        return self.rank().head(n)

    def bottom(self,
               n=5):

        return self.rank().tail(n)

    def best(self):

        return self.rank().iloc[0]

    def worst(self):

        return self.rank().iloc[-1]

    def percentile(self,
                   metric):

        return self.results[metric].rank(
            pct=True
        )

    def leaderboard(self):

        return self.rank()

    def save_csv(
            self,
            filename):

        self.rank().to_csv(
            filename,
            index=False
        )

    def save_excel(
            self,
            filename):

        self.rank().to_excel(
            filename,
            index=False
        )
