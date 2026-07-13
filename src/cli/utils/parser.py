"""
CLI parsing helpers.
"""

from __future__ import annotations

import argparse


def build_parser(description: str = "CircuitBench CLI") -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Display CLI version.",
    )

    return parser


def parse_args(parser: argparse.ArgumentParser | None = None):
    if parser is None:
        parser = build_parser()

    return parser.parse_args()
