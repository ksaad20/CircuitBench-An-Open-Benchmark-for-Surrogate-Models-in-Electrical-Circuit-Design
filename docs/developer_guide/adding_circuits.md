# Adding Circuits

## Overview

This guide describes the recommended process for adding circuit designs to Circuit-Bench. Consistent organization and documentation improve reproducibility, benchmarking quality, and long-term maintainability.

Circuit-Bench supports a wide range of circuit types, including analog, digital, RF, power electronics, passive, and mixed-signal designs.

---

# Guiding Principles

Every circuit contributed to Circuit-Bench should be:

* Correct
* Reproducible
* Well documented
* Properly licensed
* Validated
* Easy to understand
* Suitable for benchmarking

---

# Before Adding a Circuit

Verify that:

* The circuit has a clearly identified source.
* Redistribution is permitted by the applicable license.
* Simulation files are complete.
* Documentation is available.
* The circuit has been validated.

If redistribution is not permitted, include metadata and instructions that reference the official source instead of copying the design into the repository.

---

# Recommended Directory Structure

Each circuit should follow a consistent structure.

```text
circuits/
└── <category>/
    └── <circuit_name>/
        ├── README.md
        ├── metadata.yaml
        ├── LICENSE
        ├── citation.bib
        ├── schematic.png
        ├── circuit.spice
        ├── netlist.spice
        ├── simulation/
        ├── waveforms/
        ├── expected/
        ├── validation/
        ├── preprocessing.md
        ├── tasks.md
        └── statistics.json
```

---

# Required Documentation

## README.md

Document:

* Circuit name
* Description
* Circuit category
* Intended purpose
* Source
* Version
* Supported simulators
* Directory contents
* Example usage

---

## metadata.yaml

Recommended fields include:

* Name
* Category
* Version
* Author
* Organization
* Source
* License
* Technology
* Simulator compatibility
* Supported benchmark tasks
* Date added

---

## citation.bib

Include a BibTeX citation whenever the circuit originates from a publication or external project.

---

## LICENSE

Clearly identify the applicable license.

If redistribution is restricted, document the official source and usage requirements.

---

# Circuit Files

Depending on the design, include appropriate source files such as:

* SPICE netlists
* Verilog
* Verilog-A
* VHDL
* Schematic files
* Layout files
* Simulation configurations

Include only files required for reproducibility.

---

# Simulation Results

Where applicable, provide:

* Reference waveforms
* Expected outputs
* Simulation settings
* Operating conditions
* Notes on assumptions

---

# Validation

Before committing a circuit:

* Verify syntax.
* Confirm successful simulation.
* Check expected outputs.
* Validate metadata.
* Ensure required documentation is complete.

---

# Naming Conventions

Use lowercase directory names with underscores.

Examples:

* cmos_inverter
* buck_converter
* low_pass_filter
* ring_oscillator
* differential_amplifier

Avoid spaces and special characters.

---

# Benchmark Tasks

Identify the benchmark tasks supported by the circuit, such as:

* Classification
* Regression
* Fault diagnosis
* Component recognition
* Parameter estimation
* Simulation
* Timing analysis
* Power estimation

Document these in `tasks.md`.

---

# Large Files

Avoid committing unnecessarily large simulation outputs.

Instead, include:

* Representative examples
* Compressed artifacts when appropriate
* Regeneration instructions

---

# Testing

Contributed circuits should pass applicable validation steps, including:

* Simulation success
* Metadata validation
* File integrity checks
* Benchmark compatibility
* Documentation review

---

# Pull Requests

Circuit contributions should include:

* Documentation
* Metadata
* Citation information
* Licensing information
* Validation results
* Any required preprocessing or conversion scripts

---

# Best Practices

* Prefer official reference designs.
* Keep metadata complete.
* Cite original authors.
* Preserve provenance.
* Document simulator versions.
* Use descriptive names.
* Include representative validation results.
* Maintain compatibility with the Circuit-Bench benchmark framework.

Following these practices helps ensure that Circuit-Bench remains a reliable, reproducible, and extensible benchmark for circuit research and engineering.

