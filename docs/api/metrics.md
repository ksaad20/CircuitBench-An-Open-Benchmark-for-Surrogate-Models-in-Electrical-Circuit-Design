# Metrics API Reference

## Overview

The Metrics API provides a standardized interface for evaluating benchmark results within Circuit-Bench. It enables users to compute, compare, aggregate, and export evaluation metrics for machine learning models, simulations, and circuit analysis tasks.

The API is designed to be modular, reproducible, and extensible, allowing researchers to implement custom metrics alongside the built-in evaluation framework.

---

# Purpose

The Metrics API enables users to:

* Compute benchmark metrics
* Compare multiple methods
* Aggregate evaluation results
* Generate summary statistics
* Export metrics
* Integrate custom evaluation functions

---

# Supported Metric Categories

The API supports metrics for:

* Classification
* Regression
* Fault diagnosis
* Signal processing
* Circuit simulation
* Runtime analysis
* Memory usage
* Power consumption
* Reliability assessment

---

# Core Interface

Typical workflow:

1. Load predictions
2. Load ground-truth labels
3. Select evaluation metrics
4. Compute results
5. Export reports

---

# Inputs

The Metrics API accepts data such as:

* Ground-truth labels
* Predicted labels
* Prediction probabilities
* Continuous predictions
* Simulation outputs
* Circuit measurements
* Runtime statistics
* Resource utilization

Input validation is performed before evaluation whenever possible.

---

# Outputs

Typical outputs include:

* Individual metric values
* Summary statistics
* Evaluation reports
* Comparison tables
* JSON results
* CSV exports
* Visualization-ready data

---

# Built-in Classification Metrics

Supported metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* Specificity
* Sensitivity
* ROC-AUC
* PR-AUC
* Matthews Correlation Coefficient
* Cohen's Kappa

---

# Built-in Regression Metrics

Supported metrics include:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)
* Median Absolute Error
* R² Score

---

# Simulation Metrics

Simulation-oriented metrics may include:

* Voltage error
* Current error
* Frequency response deviation
* Ripple
* Power loss
* Efficiency
* Delay
* Settling time

---

# Performance Metrics

The API can also evaluate computational performance, including:

* Execution time
* CPU utilization
* GPU utilization
* Peak memory usage
* Model size
* Throughput
* Latency

---

# Metric Aggregation

Multiple benchmark runs can be aggregated using:

* Mean
* Median
* Minimum
* Maximum
* Standard deviation
* Confidence intervals

Aggregation improves comparison across repeated experiments.

---

# Custom Metrics

Users may extend the API by implementing custom metrics.

Custom metrics should:

* Accept standardized inputs.
* Return deterministic outputs.
* Include documentation.
* Be accompanied by unit tests.

---

# Error Handling

The Metrics API should detect common issues such as:

* Missing predictions
* Missing labels
* Shape mismatches
* Invalid numeric values
* Unsupported metric names
* Empty datasets

Meaningful error messages improve usability and debugging.

---

# Best Practices

When using the Metrics API:

* Validate inputs before evaluation.
* Use appropriate metrics for each task.
* Report multiple complementary metrics.
* Preserve evaluation configuration.
* Record software versions.
* Archive benchmark outputs.

---

# Related Documentation

Additional documentation includes:

* Theory: Metrics
* API: Benchmarks
* API: Reports
* API: Visualization
* Tutorials: Submit Results
* Tutorials: Generate Reports

---

# Summary

The Metrics API provides a consistent and extensible framework for benchmark evaluation within Circuit-Bench. By standardizing metric computation, aggregation, and reporting, it enables transparent comparison of algorithms, reproducible experimentation, and reliable performance assessment across diverse circuit benchmarking tasks.

