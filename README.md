# CircuitBench-An-Open-Benchmark-for-Surrogate-Models-in-Electrical-Circuit-Design-
CircuitBench is an open-source benchmark designed to provide a standardized platform for evaluating machine learning algorithms in electrical circuit analysis, optimization, and surrogate modeling. The project addresses the lack of a unified evaluation framework for AI-driven electrical engineering design by integrating reproducible circuit simulations, curated datasets, standardized performance metrics, and reference implementations of state-of-the-art machine learning models.

The benchmark contains a diverse collection of analog, digital, power electronic, RF, and passive circuit topologies simulated using open-source SPICE engines. Each circuit is evaluated under extensive parameter sweeps to generate high-quality datasets describing electrical behavior, including voltage, current, frequency response, transient response, efficiency, power dissipation, stability, and harmonic distortion.

CircuitBench enables researchers to compare machine learning models for a wide range of electrical engineering tasks, including:

1. Circuit performance prediction
2. Component parameter estimation
3. Automatic circuit optimization
4. Fault diagnosis
5. Sensitivity analysis
6. Surrogate modeling for accelerated simulation
7. Explainable artificial intelligence in circuit design

The framework supports both classical machine learning and modern deep learning approaches, allowing direct comparison between algorithms such as:

1. Linear Regression
2. Random Forest
3. Gradient Boosting
4. XGBoost
5. CatBoost
6. Support Vector Regression
7. Artificial Neural Networks
8. Graph Neural Networks
9. Physics-Informed Neural Networks
10. Gaussian Process Regression

Each algorithm is evaluated using standardized regression and classification metrics together with engineering-specific criteria, including prediction accuracy, computational efficiency, inference latency, robustness, calibration, uncertainty estimation, and interpretability.

CircuitBench emphasizes complete reproducibility through open datasets, executable notebooks, automated simulation pipelines, Docker environments, and transparent evaluation protocols.

The long-term goal of CircuitBench is to establish a community benchmark analogous to ImageNet for computer vision or GLUE for natural language processing, enabling rigorous and reproducible comparison of artificial intelligence methods for electrical engineering design.

Potential modules

1. CircuitBench-Core

Passive circuits
RLC networks
Resonance
Filters

2. CircuitBench-Analog

Operational amplifiers
Oscillators
Instrumentation amplifiers
Active filters

3. CircuitBench-Digital

CMOS logic
Timing analysis
Noise margin
Propagation delay

4. CircuitBench-Power

DC–DC converters
Inverters
Battery management circuits
Motor drives

5. CircuitBench-RF

Matching networks
Amplifiers
Transmission lines
Antennas

6. CircuitBench-Fault

Open circuits
Short circuits
Component degradation
Sensor failures

7. CircuitBench-XAI

SHAP
LIME
Feature importance
Uncertainty estimation

