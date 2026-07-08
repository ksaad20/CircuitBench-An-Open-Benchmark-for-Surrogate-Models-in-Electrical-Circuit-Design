from sklearn.metrics import (
    r2_score,
    explained_variance_score
)

def r2_score_metric(
        y_true,
        y_pred):
    """
    Coefficient of Determination (R²).
    """

    return float(
        r2_score(
            y_true,
            y_pred
        )
    )


def adjusted_r2(
        y_true,
        y_pred,
        n_features):
    """
    Adjusted R².
    """

    n = len(y_true)

    r2 = r2_score(
        y_true,
        y_pred
    )

    return float(

        1 -

        (1 - r2)

        *

        (

            (n - 1)

            /

            (n - n_features - 1)

        )

    )

def explained_variance(
        y_true,
        y_pred):
    """
    Explained Variance Score.
    """

    return float(

        explained_variance_score(

            y_true,

            y_pred

        )

    )

def variance_accounted_for(
        y_true,
        y_pred):
    """
    Variance Accounted For (VAF).
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.var(
        y_true - y_pred
    )

    denominator = np.var(
        y_true
    )

    if denominator == 0:

        return np.nan

    return float(

        (1 - numerator / denominator)

        * 100

    )

def coefficient_of_determination(
        y_true,
        y_pred):
    """
    Alias for R².
    """

    return r2_score_metric(

        y_true,

        y_pred

    )

def prediction_efficiency(
        y_true,
        y_pred):
    """
    Prediction Efficiency.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum(

        (y_true - y_pred) ** 2

    )

    denominator = np.sum(

        (

            y_true -

            np.mean(y_true)

        ) ** 2

    )

    if denominator == 0:

        return np.nan

    return float(

        1 -

        numerator /

        denominator

    )

def coefficient_of_efficiency(
        y_true,
        y_pred):
    """
    Coefficient of Efficiency.
    Equivalent to Nash-Sutcliffe.
    """

    return prediction_efficiency(

        y_true,

        y_pred

          )


def nash_sutcliffe_efficiency(
        y_true,
        y_pred):
    """
    Nash-Sutcliffe Efficiency (NSE).
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum(

        (y_true - y_pred) ** 2

    )

    denominator = np.sum(

        (

            y_true -

            np.mean(y_true)

        ) ** 2

    )

    if denominator == 0:

        return np.nan

    return float(

        1 -

        numerator /

        denominator

          )

def willmott_index(
        y_true,
        y_pred):
    """
    Willmott's Index of Agreement.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum(

        (y_pred - y_true) ** 2

    )

    denominator = np.sum(

        (

            np.abs(

                y_pred -

                np.mean(y_true)

            )

            +

            np.abs(

                y_true -

                np.mean(y_true)

            )

        ) ** 2

    )

    if denominator == 0:

        return np.nan

    return float(

        1 -

        numerator /

        denominator

          )

def kling_gupta_efficiency(
        y_true,
        y_pred):
    """
    Kling-Gupta Efficiency (KGE).
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    r = np.corrcoef(

        y_true,

        y_pred

    )[0, 1]

    alpha = (

        np.std(y_pred)

        /

        np.std(y_true)

    )

    beta = (

        np.mean(y_pred)

        /

        np.mean(y_true)

    )

    return float(

        1 -

        np.sqrt(

            (r - 1) ** 2 +

            (alpha - 1) ** 2 +

            (beta - 1) ** 2

        )

          )

__all__ = [
    # Coefficient of Determination
    "r2_score_metric",
    "adjusted_r2",
    "predicted_r2",
    "cross_validated_r2",

    # Variance Explained
    "explained_variance",
    "explained_variance_ratio",
    "variance_accounted_for",

    # Hydrological / Environmental Metrics
    "nash_sutcliffe_efficiency",
    "modified_nash_sutcliffe_efficiency",
    "kling_gupta_efficiency",
    "willmott_index",
    "refined_willmott_index",
    "legates_mccabe_index",

    # Agreement Metrics
    "index_of_agreement",
    "coefficient_of_efficiency",
    "coefficient_of_determination",

    # Information Criteria
    "akaike_information_criterion",
    "corrected_aic",
    "bayesian_information_criterion",
    "hannan_quinn_criterion",

    # Likelihood
    "log_likelihood",
    "negative_log_likelihood",
    "deviance",

    # Fit Statistics
    "chi_square_goodness_of_fit",
    "reduced_chi_square",
    "f_statistic",
    "model_significance",

    # Residual Fit
    "residual_sum_of_squares",
    "total_sum_of_squares",
    "explained_sum_of_squares",
    "mean_squared_residual",

    # Correlation-Based
    "pearson_fit",
    "spearman_fit",
    "kendall_fit",

    # Summary
    "goodness_of_fit_summary",
]
