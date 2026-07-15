from __future__ import annotations

import typer

app = typer.Typer(help="Reporting commands.")


@app.command("generate")
def generate() -> None:
    typer.echo("Report generated.")


if __name__ == "__main__":
    app()
