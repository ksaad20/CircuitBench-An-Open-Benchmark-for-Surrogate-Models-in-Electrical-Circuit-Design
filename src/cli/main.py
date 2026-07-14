from __future__ import annotations

import typer

from src.cli.commands.create import app as create_app
from src.cli.commands.version import app as version_app

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=False,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")


@app.callback(invoke_without_command=True)
def callback() -> None:
    """Run the CLI application."""
    pass


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
