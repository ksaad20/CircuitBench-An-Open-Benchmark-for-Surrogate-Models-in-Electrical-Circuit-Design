"""Circuit-Bench API server.

This module exposes information about the public API surface.

Future releases may replace or extend this implementation with a
FastAPI or similar HTTP server while preserving the public interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


__all__ = [
    "APIInfo",
    "APIServer",
    "create_server",
]


@dataclass(frozen=True)
class APIInfo:
    """Metadata describing a Circuit-Bench API."""

    name: str
    version: str
    description: str


class APIServer:
    """Lightweight registry for Circuit-Bench APIs."""

    def __init__(self) -> None:
        self._apis: Dict[str, APIInfo] = {}

        self.register(
            "benchmarks",
            "0.0.2",
            "Benchmark execution and evaluation API.",
        )
        self.register(
            "circuits",
            "0.0.2",
            "Circuit loading and management API.",
        )
        self.register(
            "datasets",
            "0.0.2",
            "Dataset discovery and loading API.",
        )
        self.register(
            "metrics",
            "0.0.2",
            "Evaluation metrics API.",
        )
        self.register(
            "models",
            "0.0.2",
            "Machine learning model API.",
        )
        self.register(
            "simulation",
            "0.0.2",
            "Circuit simulation API.",
        )
        self.register(
            "visualizations",
            "0.0.2",
            "Visualization and plotting API.",
        )
        self.register(
            "reports",
            "0.0.2",
            "Report generation API.",
        )

    def register(
        self,
        name: str,
        version: str,
        description: str,
    ) -> None:
        """Register an API."""

        self._apis[name] = APIInfo(
            name=name,
            version=version,
            description=description,
        )

    def get(self, name: str) -> APIInfo:
        """Return information for one API."""
        return self._apis[name]

    def list(self) -> List[APIInfo]:
        """Return all registered APIs."""
        return sorted(
            self._apis.values(),
            key=lambda api: api.name,
        )

    def names(self) -> List[str]:
        """Return API names."""
        return sorted(self._apis.keys())

    def count(self) -> int:
        """Return number of registered APIs."""
        return len(self._apis)


def create_server() -> APIServer:
    """Create a default API server."""
    return APIServer()


if __name__ == "__main__":
    server = create_server()

    print("Circuit-Bench API Server")
    print("-" * 30)

    for api in server.list():
        print(f"{api.name:15} {api.version:8} {api.description}")

    print("-" * 30)
    print(f"Total APIs: {server.count()}")
