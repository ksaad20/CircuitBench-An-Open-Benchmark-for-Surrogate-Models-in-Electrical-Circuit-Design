"""
Utility function tests.
"""

from pathlib import Path


def test_repository_structure():

    folders = [
        "datasets",
        "docs",
        "circuits",
        "benchmarks",
        "tests",
    ]

    for folder in folders:
        assert Path(folder).exists()
