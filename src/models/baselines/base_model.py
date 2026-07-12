"""
CircuitBench Baseline Model

Base class for all baseline models.
"""

from __future__ import annotations

from abc import ABC

from src.models.base import BaseModel


class BaselineModel(BaseModel, ABC):
    """
    Abstract base class for baseline models.
    """

    def __init__(
        self,
        name=None,
        random_state=42,
    ):
        super().__init__(
            name=name,
            random_state=random_state,
        )

    def fit(self, X, y):

        self.is_fitted = True

        return self

    def score(self, X, y):

        predictions = self.predict(X)

        try:
            from sklearn.metrics import r2_score

            return r2_score(
                y,
                predictions,
            )

        except Exception:
            return 0.0
