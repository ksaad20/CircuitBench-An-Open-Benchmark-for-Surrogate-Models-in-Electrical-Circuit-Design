"""
Project path utilities.
"""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

BENCHMARKS_DIR = PROJECT_ROOT / "benchmarks"
DATASETS_DIR = PROJECT_ROOT / "datasets"
REPORTS_DIR = PROJECT_ROOT / "reports"
CONFIGS_DIR = PROJECT_ROOT / "configs"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCS_DIR = PROJECT_ROOT / "docs"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def project_root() -> Path:
    return PROJECT_ROOT


def resolve(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)
