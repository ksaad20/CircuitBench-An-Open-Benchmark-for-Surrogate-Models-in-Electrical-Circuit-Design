"""
CircuitBench Explainability Package
===================================

Explainability and model interpretation utilities.

Modules
-------
- permutation_importance
- shap_wrapper
- partial_dependence
- ice
"""

from .permutation_importance import PermutationImportance
from .shap_wrapper import SHAPWrapper
from .partial_dependence import PartialDependence

__all__ = [
    "PermutationImportance",
    "SHAPWrapper",
    "PartialDependence",
]
