# Tutorial 01: Creating Your First Benchmark

## Overview

Welcome to Circuit-Bench.

This tutorial walks through the process of creating, configuring, and running your first benchmark. By the end of this guide, you will understand the basic benchmark workflow, required files, recommended project structure, and how to validate your benchmark.

---

# Learning Objectives

After completing this tutorial, you will be able to:

* Understand the Circuit-Bench benchmark structure.
* Create a new benchmark directory.
* Add the required metadata and documentation.
* Organize datasets and example files.
* Execute a benchmark using the command-line interface.
* Interpret the generated results.

---

# Prerequisites

Before starting, ensure that you have:

* Installed Circuit-Bench.
* Cloned the repository.
* Installed the project dependencies.
* Verified your installation using the project's diagnostic tools.

---

# Step 1: Create a Benchmark Directory

Create a new directory inside the `benchmarks` folder.

Example:

```text id="u74l6v"
benchmarks/
└── my_first_benchmark/
```

---

# Step 2: Create the Benchmark Structure

A minimal benchmark should include:

```text id="yrh2ku"
my_first_benchmark/
├── README.md
├── benchmark.yaml
├── metadata.yaml
├── datasets/
├── examples/
├── scripts/
├── results/
└── tests/
```

Additional files such as evaluation protocols, baseline descriptions, and reports can be added as the benchmark evolves.

---

# Step 3: Document the Benchmark

Your `README.md` should explain:

* Benchmark objective
* Target circuit category
* Expected inputs
* Expected outputs
* Evaluation metrics
* Usage instructions

Good documentation makes benchmarks easier to reproduce and extend.

---

# Step 4: Add Metadata

Create a `metadata.yaml` file containing information such as:

* Benchmark name
* Version
* Authors
* Supported tasks
* Dataset dependencies
* License
* Keywords

Metadata enables automated discovery and validation.

---

# Step 5: Prepare a Dataset

Select an appropriate dataset for your benchmark.

Document:

* Source
* License
* Citation
* Version
* Directory layout
* Preprocessing steps

Whenever possible, reference the official dataset source rather than redistributing third-party content.

---

# Step 6: Configure the Benchmark

Create a `benchmark.yaml` configuration describing:

* Input data
* Output location
* Evaluation metrics
* Benchmark parameters
* Reporting options

Keeping configuration separate from implementation improves reproducibility.

---

# Step 7: Run the Benchmark

Execute the benchmark using the Circuit-Bench command-line interface.

Refer to the CLI documentation for the command syntax supported by your installed version.

After execution, review the generated outputs in the configured results directory.

---

# Step 8: Validate Results

Confirm that:

* The benchmark completed successfully.
* Expected outputs were generated.
* Metrics were calculated correctly.
* Reports were produced.
* Documentation matches the observed behavior.

---

# Step 9: Interpret the Results

Typical benchmark outputs may include:

* Performance metrics
* Runtime statistics
* Resource usage
* Evaluation summaries
* Validation reports

Interpret results in the context of the benchmark objective and document any assumptions.

---

# Troubleshooting

Common issues include:

* Missing datasets
* Invalid metadata
* Configuration errors
* Unsupported file formats
* Missing dependencies

Consult the developer guides and project documentation for additional assistance.

---

# Next Steps

After completing your first benchmark, consider:

* Adding additional datasets.
* Implementing baseline methods.
* Expanding evaluation metrics.
* Improving documentation.
* Adding automated tests.
* Sharing reproducible benchmark results.

---

# Summary

You have learned how to:

* Create a benchmark structure.
* Document a benchmark.
* Organize datasets.
* Configure benchmark metadata.
* Execute a benchmark.
* Validate and interpret results.

These foundational steps provide a solid basis for developing more advanced benchmarks within Circuit-Bench.

