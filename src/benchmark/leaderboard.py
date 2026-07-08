"""
Leaderboard generation.
"""

import pandas as pd

from .ranking import RankingEngine


class Leaderboard:

    def __init__(self):

        self.engine=RankingEngine()

    def generate(self,results):

        df=pd.DataFrame(results)

        return self.engine.rank(df)
