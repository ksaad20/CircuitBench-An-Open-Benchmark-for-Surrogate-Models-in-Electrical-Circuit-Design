"""
List commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Listing commands.")


@app.command("benchmarks")
def benchmarks() -> None:
    """
    List available benchmarks.
    """
    typer.echo("No benchmarks found.")


# Backward compatibility
command = benchmarks
execute = benchmarks


def register(cli) -> None:
    """
    Register the listing commands with the CLI.
    """
    cli.add_typer(app, name="list")


if __name__ == "__main__":
    app()
