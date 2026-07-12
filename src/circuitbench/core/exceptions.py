"""
CircuitBench Exceptions
=======================

Custom exception hierarchy for CircuitBench.
"""


class CircuitBenchError(Exception):
    """Base exception for all CircuitBench errors."""

    pass


class DatasetError(CircuitBenchError):
    """Raised when dataset loading or processing fails."""

    pass


class BenchmarkError(CircuitBenchError):
    """Raised when benchmark execution fails."""

    pass


class ConfigurationError(CircuitBenchError):
    """Raised when configuration is invalid."""

    pass


class ModelError(CircuitBenchError):
    """Raised when a model cannot be trained or evaluated."""

    pass


class SimulationError(CircuitBenchError):
    """Raised when a simulator fails."""

    pass


class RegistryError(CircuitBenchError):
    """Raised when registry operations fail."""

    pass


class ValidationError(CircuitBenchError):
    """Raised when validation fails."""

    pass
