"""
CircuitBench Gradient Boosting Regressor
========================================

Production-quality wrapper around sklearn GradientBoostingRegressor.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class GradientBoostingRegressionModel(SklearnModel):
    """
    Gradient Boosting Regression.
    """

    def __init__(
        self,
        loss: str = "squared_error",
        learning_rate: float = 0.1,
        n_estimators: int = 100,
        subsample: float = 1.0,
        criterion: str = "friedman_mse",
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        max_depth: int = 3,
        random_state: int = 42,
    ):

        estimator = GradientBoostingRegressor(
            loss=loss,
            learning_rate=learning_rate,
            n_estimators=n_estimators,
            subsample=subsample,
            criterion=criterion,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_depth=max_depth,
            random_state=random_state,
        )

        super().__init__(
            estimator=estimator,
            name="GradientBoostingRegression",
            random_state=random_state,
        )

    # --------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update({
            "learning_rate": self.model.learning_rate,
            "n_estimators": self.model.n_estimators,
            "subsample": self.model.subsample,
            "loss": self.model.loss,
            "criterion": self.model.criterion,
            "max_depth": self.model.max_depth,
        })

        return self

    # --------------------------------------------------

    def feature_importance(self):

        importance = np.asarray(
            self.model.feature_importances_,
            dtype=float,
        )

        total = importance.sum()

        if total == 0:
            return importance

        return importance / total

    # --------------------------------------------------

    def staged_predictions(self, X):

        return self.model.staged_predict(X)

    # --------------------------------------------------

    def training_loss(self):

        return getattr(
            self.model,
            "train_score_",
            None,
        )

    # --------------------------------------------------

    def summary(self):

        print("=" * 70)
        print("CircuitBench Gradient Boosting")
        print("=" * 70)

        for key, value in self.metadata.items():
            print(f"{key:20}: {value}")

        print("=" * 70)

    # --------------------------------------------------

    def __repr__(self):

        return (
            "GradientBoostingRegressionModel("
            f"estimators={self.model.n_estimators}, "
            f"lr={self.model.learning_rate}, "
            f"fitted={self.is_fitted})"
        )


__all__ = [
    "GradientBoostingRegressionModel",
]
