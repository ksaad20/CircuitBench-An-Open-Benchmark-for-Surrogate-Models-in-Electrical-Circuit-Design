"""
CircuitBench Scikit-Learn Base Model
====================================

Abstract wrapper for scikit-learn estimators.

All classical machine learning models should inherit from this class.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from abc import ABC

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from src.models.base import BaseModel


class SklearnModel(BaseModel, ABC):
    """
    Base wrapper for all scikit-learn models.
    """

    def __init__(
        self,
        estimator,
        name: str,
        random_state: int = 42,
    ):

        super().__init__(
            name=name,
            random_state=random_state,
        )

        self.model = estimator

    # -----------------------------------------------------

    def fit(self, X, y):

        self.model.fit(X, y)

        self.is_fitted = True

        self.metadata = {
            "n_samples": X.shape[0],
            "n_features": X.shape[1],
        }

        return self

    # -----------------------------------------------------

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return self.model.predict(X)

    # -----------------------------------------------------

    def score(self, X, y):

        return float(
            r2_score(
                y,
                self.predict(X),
            )
        )

    # -----------------------------------------------------

    def evaluate(self, X, y):

        prediction = self.predict(X)

        mse = mean_squared_error(
            y,
            prediction,
        )

        return {
            "R2": float(
                r2_score(
                    y,
                    prediction,
                )
            ),
            "MAE": float(
                mean_absolute_error(
                    y,
                    prediction,
                )
            ),
            "MSE": float(mse),
            "RMSE": float(np.sqrt(mse)),
        }

    # -----------------------------------------------------

    def coefficients(self):

        if hasattr(self.model, "coef_"):
            return self.model.coef_

        raise AttributeError("Estimator has no coefficients.")

    # -----------------------------------------------------

    def intercept(self):

        if hasattr(self.model, "intercept_"):
            return self.model.intercept_

        raise AttributeError("Estimator has no intercept.")

    # -----------------------------------------------------

    def feature_importance(self):

        if hasattr(self.model, "feature_importances_"):

            importance = np.asarray(
                self.model.feature_importances_,
                dtype=float,
            )

        elif hasattr(self.model, "coef_"):

            importance = np.abs(
                np.asarray(
                    self.model.coef_,
                    dtype=float,
                )
            )

        else:

            raise AttributeError(
                "Estimator exposes neither feature_importances_ nor coef_."
            )

        total = importance.sum()

        if total == 0:

            return importance

        return importance / total

    # -----------------------------------------------------

    def get_params(self):

        return self.model.get_params()

    # -----------------------------------------------------

    def set_params(self, **kwargs):

        self.model.set_params(**kwargs)

        return self

    # -----------------------------------------------------

    def summary(self):

        print("=" * 70)

        print(self.name)

        print("=" * 70)

        for key, value in self.metadata.items():

            print(f"{key:20}: {value}")

        print("=" * 70)

    # -----------------------------------------------------

    def __repr__(self):

        return f"{self.__class__.__name__}" f"(fitted={self.is_fitted})"


__all__ = [
    "SklearnModel",
]
