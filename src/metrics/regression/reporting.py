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

def bootstrap_confidence_interval(
        values,
        n_bootstrap=1000,
        confidence=0.95):
    """
    Bootstrap confidence interval.
    """

    values = np.asarray(values)

    estimates = []

    for _ in range(n_bootstrap):

        sample = np.random.choice(

            values,

            len(values),

            replace=True

        )

        estimates.append(

            np.mean(sample)

        )

    alpha = (1 - confidence) / 2

    return (

        np.percentile(

            estimates,

            100 * alpha

        ),

        np.percentile(

            estimates,

            100 * (1 - alpha)

        )

    )

def regression_scorecard(
        y_true,
        y_pred):
    """
    Compact regression report.
    """

    return {

        "MAE":

        mean_absolute_error(

            y_true,

            y_pred

        ),

        "MSE":

        mean_squared_error(

            y_true,

            y_pred

        ),

        "RMSE":

        root_mean_squared_error(

            y_true,

            y_pred

        ),

        "R2":

        r2_score_metric(

            y_true,

            y_pred

        ),

        "MAPE":

        mean_absolute_percentage_error(

            y_true,

            y_pred

        )

}

def compare_regression_models(
        results):
    """
    Compare multiple regression models.
    """

    return leaderboard(results)

def regression_report(
        y_true,
        y_pred):
    """
    Comprehensive regression report.
    """

    return {

        "Errors":

        regression_scorecard(

            y_true,

            y_pred

        ),

        "Residuals":

        residual_summary(

            y_true,

            y_pred

        )

    }

def metric_dictionary():
    """
    Return supported regression metrics.
    """

    return [

        "MAE",

        "MSE",

        "RMSE",

        "MAPE",

        "SMAPE",

        "R2",

        "Adjusted R2",

        "Explained Variance",

        "NSE",

        "KGE"

    ]

def validate_regression_inputs(
        y_true,
        y_pred):
    """
    Validate regression inputs.
    """

    if len(y_true) != len(y_pred):

        raise ValueError(

            "Input lengths differ."

        )

    return True

def regression_metrics_dataframe(
        report):
    """
    Convert report dictionary
    to DataFrame.
    """

    return pd.DataFrame(

        report,

        index=[0]

    )

def export_regression_csv(
        dataframe,
        filename):
    """
    Export metrics.
    """

    dataframe.to_csv(

        filename,

        index=False

    )

def regression_benchmark_report(
        results):
    """
    Complete benchmark report.
    """

    return {

        "Leaderboard":

        leaderboard(results),

        "Summary":

        benchmark_summary(results)

    }

def regression_pipeline(
        y_true,
        y_pred):
    """
    Complete evaluation pipeline.
    """

    return {

        "Metrics":

        regression_scorecard(

            y_true,

            y_pred

        ),

        "Residuals":

        residual_summary(

            y_true,

            y_pred

        ),

        "Diagnostics":

        residual_normality_report(

            y_true,

            y_pred

        )

    }

__all__ = [
    "regression_report",
    "classification_report",
    "benchmark_report",
    "summary_report",

    "metrics_table",
    "latex_table",
    "markdown_table",
    "html_table",
    "csv_table",

    "export_csv",
    "export_json",
    "export_excel",
    "export_yaml",
    "export_pickle",

    "leaderboard",
    "rank_models",
    "best_model",
    "worst_model",
    "top_k_models",

    "benchmark_summary",
    "comparison_report",
    "aggregate_report",
    "statistical_report",

    "scorecard",
    "performance_dashboard_data",
    "metric_heatmap_data",
    "correlation_matrix_data",
    "confusion_matrix_report",

    "publication_table",
    "supplementary_table",
    "appendix_metrics",
    "citation_summary",

    "report_to_dataframe",
    "report_to_dict",
    "merge_reports",
    "compare_reports",
    "pretty_print_report",
]
