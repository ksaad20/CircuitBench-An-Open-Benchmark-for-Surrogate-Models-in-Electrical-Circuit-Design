from __future__ import annotations

import typer

app = typer.Typer(help="Evaluation commands.")


@app.command("run")
def run() -> None:
    typer.echo("Evaluation completed.")


if __name__ == "__main__":
    app()
