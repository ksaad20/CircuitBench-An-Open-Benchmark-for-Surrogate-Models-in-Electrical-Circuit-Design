"""
Reporting utilities for CircuitBench.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BenchmarkReport:
    """Simple benchmark report."""

    title: str = "CircuitBench Report"
    results: Dict[str, Any] | None = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "results": self.results or {},
        }

    def summary(self) -> str:
        return f"{self.title}: {len(self.results or {})} result(s)"
