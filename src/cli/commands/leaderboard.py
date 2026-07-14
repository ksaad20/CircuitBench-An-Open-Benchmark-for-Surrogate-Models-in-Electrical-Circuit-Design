"""Leaderboard command."""

from __future__ import annotations


def leaderboard(args) -> None:
    """Display the benchmark leaderboard."""
    if hasattr(args, "results"):
        print(f"Displaying leaderboard for {args.results}")
    else:
        print("Displaying benchmark leaderboard.")


# Backward compatibility
execute = leaderboard
