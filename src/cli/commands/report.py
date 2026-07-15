"""
Report commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Generate benchmark reports.")


@app.command("generate")
def report(output: str = "report.txt") -> None:
    """
    Generate a benchmark report.
    """
    typer.echo(f"Generating benchmark report: {output}")


@app.command("summary")
def summary() -> None:
    """
    Display a report summary.
    """
    typer.echo("Report summary is not yet implemented.")


@app.command("export")
def export(filename: str = "report.json") -> None:
    """
    Export a report.
    """
    typer.echo(f"Exporting report to {filename}")


# Backward compatibility
command = report
execute = report


def register(cli) -> None:
    """
    Compatibility registration function.
    """
    cli.add_typer(app, name="report")
