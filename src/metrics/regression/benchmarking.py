def rank_models(
        results,
        ascending=True):
    """
    Rank regression models by metric.

    Parameters
    ----------
    results : dict
        Mapping of model names to scores.
    ascending : bool
        True for error metrics (lower is better),
        False for score metrics (higher is better).
    """

    return sorted(

        results.items(),

        key=lambda x: x[1],

        reverse=not ascending

    )

def best_model(
        results,
        ascending=True):
    """
    Return the best model.
    """

    ranking = rank_models(

        results,

        ascending

    )

    return ranking[0]


def worst_model(
        results,
        ascending=True):
    """
    Return the worst model.
    """

    ranking = rank_models(

        results,

        ascending

    )

    return ranking[-1]


def aggregate_scores(
        dataframe):
    """
    Average each model's metrics.
    """

    return dataframe.mean()

def normalize_scores(
        scores):
    """
    Min-Max normalization.
    """

    scores = np.asarray(scores)

    return (

        scores -

        scores.min()

    ) / (

        scores.max()

        -

        scores.min()

    )



def weighted_score(
        scores,
        weights):
    """
    Weighted aggregate score.
    """

    scores = np.asarray(scores)

    weights = np.asarray(weights)

    return float(

        np.average(

            scores,

            weights=weights

        )

    )


def geometric_mean_score(
        scores):
    """
    Geometric mean.
    """

    scores = np.asarray(scores)

    scores = np.maximum(

        scores,

        1e-12

    )

    return float(

        np.exp(

            np.mean(

                np.log(scores)

            )

        )

    )


def harmonic_mean_score(
        scores):
    """
    Harmonic mean.
    """

    scores = np.asarray(scores)

    return float(

        len(scores)

        /

        np.sum(

            1 / scores

        )

    )


def leaderboard(
        results,
        ascending=True):
    """
    Return leaderboard DataFrame.
    """

    ranking = rank_models(

        results,

        ascending

    )

    return pd.DataFrame(

        ranking,

        columns=[

            "Model",

            "Score"

        ]

    )

def benchmark_summary(
        results,
        ascending=True):
    """
    Benchmark summary.
    """

    return {

        "Best":

        best_model(

            results,

            ascending

        ),

        "Worst":

        worst_model(

            results,

            ascending

        ),

        "Mean":

        float(

            np.mean(

                list(results.values())

            )

        ),

        "Std":

        float(

            np.std(

                list(results.values())

            )

        )

    }

__all__ = [
    # Model Evaluation
    "evaluate_model",
    "evaluate_models",
    "benchmark_model",
    "benchmark_models",
    "cross_validate_model",

    # Benchmark Summary
    "benchmark_summary",
    "benchmark_report",
    "benchmark_statistics",
    "benchmark_overview",
    "benchmark_dataframe",

    # Rankings
    "rank_models",
    "leaderboard",
    "best_model",
    "worst_model",
    "top_k_models",
    "bottom_k_models",
    "model_rank",

    # Model Comparison
    "compare_models",
    "pairwise_comparison",
    "relative_improvement",
    "percentage_improvement",
    "performance_difference",

    # Aggregation
    "aggregate_metrics",
    "aggregate_scores",
    "weighted_score",
    "normalized_score",
    "geometric_score",
    "harmonic_score",

    # Stability
    "benchmark_stability",
    "benchmark_consistency",
    "performance_variance",
    "performance_std",

    # Efficiency
    "benchmark_runtime",
    "benchmark_memory",
    "benchmark_energy",
    "benchmark_latency",

    # Robustness
    "benchmark_noise",
    "benchmark_outliers",
    "benchmark_missing_values",
    "benchmark_distribution_shift",

    # Statistical Benchmarking
    "confidence_ranking",
    "bootstrap_benchmark",
    "cross_dataset_benchmark",
    "significance_ranking",

    # Utilities
    "save_benchmark",
    "load_benchmark",
    "export_benchmark",
    "benchmark_to_dataframe",
    "benchmark_to_dict",
]

