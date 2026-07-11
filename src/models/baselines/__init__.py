"""
CircuitBench Baseline Models
============================

Collection of baseline models used as reference methods for
benchmarking surrogate models.

Available Models
----------------
Regression
~~~~~~~~~~
- MeanPredictor
- MedianPredictor
- ConstantPredictor
- RandomPredictor

Classification
~~~~~~~~~~~~~~
- ModePredictor
"""

from .base_model import BaselineModel
from .base_regressor import BaselineRegressor
from .base_classifier import BaselineClassifier

from .mean_predictor import MeanPredictor
from .median_predictor import MedianPredictor
from .constant_predictor import ConstantPredictor
from .random_predictor import RandomPredictor
from .mode_predictor import ModePredictor

__version__ = "0.1.0"

BASELINE_MODELS = {
    "MeanPredictor": MeanPredictor,
    "MedianPredictor": MedianPredictor,
    "ConstantPredictor": ConstantPredictor,
    "RandomPredictor": RandomPredictor,
    "ModePredictor": ModePredictor,
}

REGRESSION_BASELINES = [
    MeanPredictor,
    MedianPredictor,
    ConstantPredictor,
    RandomPredictor,
]

CLASSIFICATION_BASELINES = [
    ModePredictor,
]

__all__ = [
    "BaselineModel",
    "BaselineRegressor",
    "BaselineClassifier",
    "MeanPredictor",
    "MedianPredictor",
    "ConstantPredictor",
    "RandomPredictor",
    "ModePredictor",
    "BASELINE_MODELS",
    "REGRESSION_BASELINES",
    "CLASSIFICATION_BASELINES",
]
