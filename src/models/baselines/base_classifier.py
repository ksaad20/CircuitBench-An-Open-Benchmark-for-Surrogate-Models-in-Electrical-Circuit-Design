"""
Baseline Classifier
"""

from __future__ import annotations

import numpy as np

from .base_model import BaselineModel


class BaselineClassifier(BaselineModel):
    """
    Parent class for baseline classifiers.
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

        self.label_ = None

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return np.full(
            len(X),
            self.label_,
        )
