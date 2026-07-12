"""
Baseline Regressor
"""

from __future__ import annotations

import numpy as np

from .base_model import BaselineModel


class BaselineRegressor(BaselineModel):
    """
    Parent class for all baseline regressors.
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

        self.constant_ = None

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return np.full(
            len(X),
            self.constant_,
            dtype=float,
        )
