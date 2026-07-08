"""
Global configuration for CircuitBench.
"""

from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parents[2]

# Dataset locations
DATA_DIR = ROOT / "datasets"

# Benchmark results
RESULTS_DIR = ROOT / "results"

# Figures
FIGURE_DIR = ROOT / "figures"

# Random seed
SEED = 42

# Default simulator
DEFAULT_SIMULATOR = "ngspice"

# Floating point precision
DTYPE = "float32"

# Default batch size
BATCH_SIZE = 32

# Logging level
LOG_LEVEL = "INFO"
