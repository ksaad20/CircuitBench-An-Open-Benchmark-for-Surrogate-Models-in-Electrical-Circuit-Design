"""
Circuit Bench CLI command package.
"""

from __future__ import annotations

from .benchmarks import benchmarks
from .cache import cache
from .clean import clean
from .config import config
from .info import info
from .plugins import plugins
from .shell import shell

__all__ = [
    "benchmarks",
    "cache",
    "clean",
    "config",
    "info",
    "plugins",
    "shell",
]
