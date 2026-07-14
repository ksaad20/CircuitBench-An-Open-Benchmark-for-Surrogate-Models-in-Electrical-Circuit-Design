"""
Console utilities for CircuitBench CLI.
"""

from __future__ import annotations


def print_info(message: str) -> None:
    print(message)


def print_success(message: str) -> None:
    print(f"✓ {message}")


def print_warning(message: str) -> None:
    print(f"WARNING: {message}")


def print_error(message: str) -> None:
    print(f"ERROR: {message}")


def print_header(title: str) -> None:
    print()
    print("=" * len(title))
    print(title)
    print("=" * len(title))
