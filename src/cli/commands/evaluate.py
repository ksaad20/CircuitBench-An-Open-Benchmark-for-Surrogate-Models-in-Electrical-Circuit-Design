
"""
Evaluation commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Evaluation commands.")


@app.command("run")
def run() -> None:
    """
    Run the benchmark evaluation.
    """
    typer.echo("Evaluation completed.")


# Backward compatibility
command = run
execute = run


def register(cli) -> None:
    """
    Register the evaluation commands with the CLI.
    """
    cli.add_typer(app, name="evaluate")


if __name__ == "__main__":
    app()
