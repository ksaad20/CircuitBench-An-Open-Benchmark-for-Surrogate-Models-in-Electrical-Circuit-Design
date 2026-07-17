# Dataset Card

## Dataset Name

Task Taxonomy

---

## Version

v1.0.0

---

## Description

The **Task Taxonomy** dataset provides a structured classification of tasks supported by Circuit-Bench. It defines standardized categories for circuit analysis, simulation, optimization, verification, benchmarking, machine learning, and educational workflows. The taxonomy promotes consistency in benchmarking, dataset annotation, task discovery, and evaluation across the repository.

---

## Purpose

This dataset is designed to:

- Standardize benchmark task definitions
- Organize datasets by task category
- Support reproducible evaluations
- Enable task-based benchmarking
- Improve dataset discoverability
- Facilitate machine learning dataset labeling
- Provide a common vocabulary for contributors

---

## Domain

- Electronic Design Automation (EDA)
- Circuit Design
- Circuit Simulation
- Analog Electronics
- Digital Electronics
- Mixed-Signal Electronics
- RF Engineering
- Power Electronics
- Scientific Computing
- Machine Learning for Circuits

---

## Task Categories

Example categories include:

### Circuit Analysis

- DC Analysis
- AC Analysis
- Transient Analysis
- Noise Analysis
- Harmonic Balance
- Sensitivity Analysis
- Operating Point Analysis

### Circuit Design

- Analog Design
- Digital Design
- RF Design
- Power Electronics Design
- Mixed-Signal Design

### Simulation

- SPICE Simulation
- Behavioral Simulation
- Monte Carlo Simulation
- Corner Analysis
- Temperature Sweep
- Parametric Sweep

### Verification

- Functional Verification
- Design Rule Checking
- Regression Testing
- Simulation Validation
- Model Verification

### Optimization

- Parameter Optimization
- Component Selection
- Power Optimization
- Area Optimization
- Performance Optimization

### Machine Learning

- Classification
- Regression
- Clustering
- Fault Detection
- Circuit Recognition
- Performance Prediction
- Surrogate Modeling

### Benchmarking

- Accuracy Evaluation
- Runtime Evaluation
- Memory Benchmarking
- Scalability Analysis
- Robustness Testing
- Reproducibility Assessment

### Education

- Tutorials
- Laboratory Exercises
- Homework Problems
- Demonstrations
- Teaching Examples

---

## File Formats

Supported formats may include:

- `.csv`
- `.json`
- `.yaml`
- `.md`

---

## Directory Structure

```text
task_taxonomy/
├── taxonomy.csv
├── taxonomy.json
├── hierarchy.yaml
├── metadata.json
└── README.md
```

---

## Example Fields

| Field | Description |
|--------|-------------|
| task_id | Unique task identifier |
| task_name | Name of the task |
| category | High-level task category |
| subcategory | More specific task grouping |
| description | Task definition |
| input_type | Expected inputs |
| output_type | Expected outputs |
| evaluation_metric | Recommended evaluation metric |
| difficulty | Estimated complexity |
| tags | Associated keywords |

---

## Applications

This dataset supports:

- Benchmark organization
- Dataset annotation
- Machine learning pipelines
- Automated benchmark selection
- Research reproducibility
- Educational content organization
- Task discovery
- Metadata standardization

---

## Evaluation

Quality may be assessed using:

- Taxonomy completeness
- Category consistency
- Coverage of supported tasks
- Metadata completeness
- Annotation accuracy
- Hierarchical consistency

---

## Limitations

- Emerging research tasks may require future taxonomy updates.
- Some tasks may belong to multiple categories.
- Domain-specific classifications may evolve over time.

---

## Reproducibility

For each task definition, document:

- Version
- Category
- Inputs
- Outputs
- Evaluation metrics
- Dependencies
- Related datasets
- Associated benchmarks

---

## FAIR Compliance

This dataset promotes:

- **Findability** through standardized task identifiers
- **Accessibility** via structured metadata
- **Interoperability** using common task definitions
- **Reusability** through consistent documentation

---

## Citation

If you use the Task Taxonomy dataset, please cite the associated Circuit-Bench publication and repository.

---

## License

Specify the applicable license (e.g., MIT, Apache-2.0, CC BY 4.0).

---

## Maintainers

Circuit-Bench Contributors

---

## Contact

Please open an issue or discussion in the repository for questions, corrections, or contributions.

---

## Changelog

### v1.0.0

- Initial release
- Introduced standardized task taxonomy
- Added hierarchical task classification
- Included metadata fields for benchmarking and reproducibility
