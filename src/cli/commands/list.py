from __future__ import annotations

import typer

app = typer.Typer(help="Listing commands.")


@app.command("benchmarks")
def benchmarks() -> None:
    typer.echo("No benchmarks found.")


if __name__ == "__main__":
    app()
