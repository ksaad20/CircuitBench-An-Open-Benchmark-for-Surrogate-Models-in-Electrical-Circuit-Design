"""
Report commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Reporting commands.")


@app.command("generate")
def generate() -> None:
    """
    Generate a benchmark report.
    """
    typer.echo("Report generated.")


# Backward compatibility
command = generate
execute = generate


def register(cli) -> None:
    """
    Register the report commands with the CLI.
    """
    cli.add_typer(app, name="report")


if __name__ == "__main__":
    app()
