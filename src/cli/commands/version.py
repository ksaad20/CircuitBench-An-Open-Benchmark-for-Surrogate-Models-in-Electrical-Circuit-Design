"""
Version command for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Display version information.")


@app.command("show")
def main() -> None:
    """
    Show the Circuit-Bench version.
    """
    typer.echo("Circuit-Bench 0.1.0")


# Backward compatibility
command = main
execute = main


def register(cli) -> None:
    """
    Register the version command with the CLI.
    """
    cli.add_typer(app, name="version")
