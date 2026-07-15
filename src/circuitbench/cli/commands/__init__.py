"""
Circuit Bench CLI commands package.

Commands are imported lazily by the CLI entry point.
"""

from __future__ import annotations

# Import the app object from your implementation file (e.g., base.py)
from .base import app 

__all__: list[str] = ["app"]
