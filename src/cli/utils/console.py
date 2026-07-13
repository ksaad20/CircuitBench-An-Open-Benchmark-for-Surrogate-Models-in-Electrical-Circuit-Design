"""
Console utilities for CircuitBench CLI.
"""

from __future__ import annotations

from rich.console import Console

console = Console()


def print_info(message: str) -> None:
    console.print(f"[cyan]{message}[/cyan]")


def print_success(message: str) -> None:
    console.print(f"[green]✔ {message}[/green]")


def print_warning(message: str) -> None:
    console.print(f"[yellow]⚠ {message}[/yellow]")


def print_error(message: str) -> None:
    console.print(f"[bold red]✖ {message}[/bold red]")


def print_header(title: str) -> None:
    console.rule(f"[bold blue]{title}")
