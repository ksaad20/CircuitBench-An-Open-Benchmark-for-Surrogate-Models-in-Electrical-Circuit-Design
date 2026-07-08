"""
Tests for benchmark loading and execution.
"""

import pytest


def test_benchmark_module_exists():
    try:
        import src.benchmark
    except Exception as e:
        pytest.fail(f"Benchmark module failed to import: {e}")


def test_available_benchmarks():
    import src.benchmark as benchmark

    assert hasattr(benchmark, "AVAILABLE_BENCHMARKS")


def test_benchmark_is_list():
    import src.benchmark as benchmark

    assert isinstance(benchmark.AVAILABLE_BENCHMARKS, list)
