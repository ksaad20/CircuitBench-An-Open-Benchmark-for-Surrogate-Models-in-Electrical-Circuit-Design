from __future__ import annotations

import typer

from circuitbench.cli.commands import (
    benchmarks_app,
    base_app,
    cache_app,
    clean_app,
    config_app,
    create_app,
    datasets_app,
    doctor_app,
    evaluate_app,
    export_app,
    info_app,
    leaderboard_app,
    list_app,
    plugins_app,
    report_app,
    run_app,
    shall_app,
    stats_app,
    validate_app,
    version_app,
)

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=False,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")
app.add_typer(doctor_app, name="doctor")
app.add_typer(benchmarks_app, name="benchmarks")
app.add_typer(cache_app, name="cache")
app.add_typer(clean_app, name="clean")
app.add_typer(config_app, name="config")
app.add_typer(datasets_app, name="datasets")
app.add_typer(evaluate_app, name="evaluate")
app.add_typer(export_app, name="export")
app.add_typer(info_app, name="info")
app.add_typer(leaderboard_app, name="leaderboard")
app.add_typer(list_app, name="list")
app.add_typer(plugins_app, name="plugins")
app.add_typer(report_app, name="report")
app.add_typer(run_app, name="run")
app.add_typer(shall_app, name="shell")
app.add_typer(stats_app, name="stats")
app.add_typer(validate_app, name="validate")


@app.callback(invoke_without_command=True)
def callback() -> None:
    """CLI callback."""
    return


def main() -> None:
    """Run the CLI."""
    app()


if __name__ == "__main__":
    main()
