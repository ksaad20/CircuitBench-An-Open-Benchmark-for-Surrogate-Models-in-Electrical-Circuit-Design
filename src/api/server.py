"""Circuit-Bench API server."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class APIInfo:
    """Information describing a public API."""

    name: str
    version: str
    description: str


class APIServer:
    """Simple registry for Circuit-Bench APIs."""

    def __init__(self) -> None:
        """Initialize the API registry."""
        self._apis: dict[str, APIInfo] = {}

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
        """Return information for a registered API."""
        return self._apis[name]

    def list(self) -> list[APIInfo]:
        """Return all registered APIs."""
        return sorted(
            self._apis.values(),
            key=lambda api: api.name,
        )

    def names(self) -> list[str]:
        """Return registered API names."""
        return sorted(self._apis)

    def count(self) -> int:
        """Return the number of registered APIs."""
        return len(self._apis)


def create_server() -> APIServer:
    """Create a server with the default API registry."""
    server = APIServer()

    server.register(
        "benchmarks",
        "0.0.2",
        "Benchmark execution API.",
    )
    server.register(
        "circuits",
        "0.0.2",
        "Circuit management API.",
    )
    server.register(
        "datasets",
        "0.0.2",
        "Dataset management API.",
    )
    server.register(
        "metrics",
        "0.0.2",
        "Metrics evaluation API.",
    )
    server.register(
        "models",
        "0.0.2",
        "Model management API.",
    )
    server.register(
        "simulation",
        "0.0.2",
        "Circuit simulation API.",
    )
    server.register(
        "visualizations",
        "0.0.2",
        "Visualization API.",
    )
    server.register(
        "reports",
        "0.0.2",
        "Report generation API.",
    )

    return server


def main() -> None:
    """Display registered APIs."""
    server = create_server()

    print("Circuit-Bench API Server")
    print("=" * 30)

    for api in server.list():
        print(f"{api.name:<16}{api.version:<8}{api.description}")

    print("=" * 30)
    print(f"Total APIs: {server.count()}")


if __name__ == "__main__":
    main()
