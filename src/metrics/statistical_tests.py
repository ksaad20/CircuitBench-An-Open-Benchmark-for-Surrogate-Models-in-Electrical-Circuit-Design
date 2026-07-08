from scipy.stats import (
    ttest_1samp,
    ttest_ind,
    ttest_rel,
    t,
    mannwhitneyu,
    wilcoxon,
    kruskal,
    friedmanchisquare,
    median_test,
    mood,
)

from scipy.stats import studentized_range
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import numpy as np

from scipy.stats import rankdata
import numpy as np

compare_models(
    model_scores,
    alpha=0.05,
    correction="holm",
    effect_size=True,
    confidence_interval=True,
    posthoc=True
)

"""
statistical_tests.py

Statistical hypothesis tests for CircuitBench.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from scipy.stats import (
    shapiro,
    anderson,
    kstest,
    jarque_bera,
    normaltest,
    levene,
)

from scipy.stats import (
    pearsonr,
    spearmanr,
    kendalltau,
    pointbiserialr,
    chi2_contingency
)

from scipy.spatial.distance import pdist, squareform
from scipy.linalg import pinv

import numpy as np
import pandas as pd

def describe(data):

    """
    Descriptive statistics.

    Parameters
    ----------
    data : array-like

    Returns
    -------
    pandas.Series
    """

    return pd.Series(data).describe()

def summary(data):

    """
    Complete descriptive summary.
    """

    x = np.asarray(data)

    return {

        "Count": len(x),

        "Mean": float(np.mean(x)),

        "Median": float(np.median(x)),

        "Minimum": float(np.min(x)),

        "Maximum": float(np.max(x)),

        "Variance": float(np.var(x, ddof=1)),

        "Standard Deviation": float(np.std(x, ddof=1)),

        "Skewness": pd.Series(x).skew(),

        "Kurtosis": pd.Series(x).kurt()

    }

def normality_report(data,
                     alpha=0.05):

    """
    Combined normality report.
    """

    report = {

        "Shapiro":

        shapiro_test(data, alpha),

        "Jarque-Bera":

        jarque_bera_test(data, alpha),

        "D'Agostino":

        dagostino_test(data, alpha)

    }

    return report

def shapiro_test(data,
                 alpha=0.05):

    """
    Shapiro-Wilk normality test.
    """

    statistic, p = shapiro(data)

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Normal": bool(p > alpha)

    }

def anderson_darling(data):

    """
    Anderson-Darling test.
    """

    result = anderson(data)

    return {

        "Statistic": float(result.statistic),

        "Critical Values":

        result.critical_values.tolist(),

        "Significance":

        result.significance_level.tolist()

    }

def kolmogorov_smirnov(data):

    """
    Kolmogorov-Smirnov test
    against the normal distribution.
    """

    statistic, p = kstest(

        data,

        "norm",

        args=(

            np.mean(data),

            np.std(data, ddof=1)

        )

    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p)

    }

def jarque_bera_test(data,
                     alpha=0.05):

    statistic, p = jarque_bera(data)

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Normal": bool(p > alpha)

    }
def dagostino_test(data,
                   alpha=0.05):

    statistic, p = normaltest(data)

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Normal": bool(p > alpha)

    }

def levene_test(*groups,
                alpha=0.05):

    """
    Equality of variance test.
    """

    statistic, p = levene(*groups)

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Equal Variance": bool(p > alpha)

    }

def assumptions_report(*groups):

    """
    Automatically evaluate
    assumptions before hypothesis testing.
    """

    report = {

        "Normality": [],

        "Equal Variance": None

    }

    for g in groups:

        report["Normality"].append(

            shapiro_test(g)

        )

    report["Equal Variance"] = \

        levene_test(*groups)

    return report


def one_sample_ttest(
        sample,
        population_mean,
        alpha=0.05):

    """
    One-sample Student's t-test.
    """

    statistic, p = ttest_1samp(
        sample,
        population_mean
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": bool(p < alpha)

    }

def independent_ttest(
        group1,
        group2,
        alpha=0.05):

    """
    Independent two-sample t-test.
    """

    statistic, p = ttest_ind(
        group1,
        group2,
        equal_var=True
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": bool(p < alpha)

    }

def paired_ttest(
        before,
        after,
        alpha=0.05):

    """
    Paired Student's t-test.
    """

    statistic, p = ttest_rel(
        before,
        after
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": bool(p < alpha)

    }

def welch_ttest(
        group1,
        group2,
        alpha=0.05):

    """
    Welch's unequal variance t-test.
    """

    statistic, p = ttest_ind(

        group1,

        group2,

        equal_var=False

    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": bool(p < alpha)

    }

def confidence_interval(
        values,
        confidence=0.95):

    """
    Confidence interval of the mean.
    """

    values = np.asarray(values)

    n = len(values)

    mean = np.mean(values)

    std = np.std(
        values,
        ddof=1
    )

    margin = t.ppf(

        (1 + confidence) / 2,

        n - 1

    ) * std / np.sqrt(n)

    return {

        "Mean": float(mean),

        "Lower": float(mean - margin),

        "Upper": float(mean + margin),

        "Confidence": confidence

    }

def pooled_variance(
        group1,
        group2):

    """
    Compute pooled variance.
    """

    n1 = len(group1)

    n2 = len(group2)

    s1 = np.var(
        group1,
        ddof=1
    )

    s2 = np.var(
        group2,
        ddof=1
    )

    return (

        ((n1 - 1) * s1)

        +

        ((n2 - 1) * s2)

    ) / (

        n1 + n2 - 2

    )

def pooled_variance(
        group1,
        group2):

    """
    Compute pooled variance.
    """

    n1 = len(group1)

    n2 = len(group2)

    s1 = np.var(
        group1,
        ddof=1
    )

    s2 = np.var(
        group2,
        ddof=1
    )

    return (

        ((n1 - 1) * s1)

        +

        ((n2 - 1) * s2)

    ) / (

        n1 + n2 - 2

    )

def standard_error_difference(
        group1,
        group2):

    """
    Standard error of difference.
    """

    sp = pooled_variance(
        group1,
        group2
    )

    return np.sqrt(

        sp *

        (

            1 / len(group1)

            +

            1 / len(group2)

        )

    )

def mean_difference(
        group1,
        group2):

    """
    Difference between group means.
    """

    return float(

        np.mean(group1)

        -

        np.mean(group2)

    )

def variance_ratio(
        group1,
        group2):

    """
    Ratio of variances.
    """

    return float(

        np.var(group1, ddof=1)

        /

        np.var(group2, ddof=1)

    )


def hypothesis_summary(
        result):

    """
    Produce a concise textual
    summary of a hypothesis test.
    """

    if result["Reject H0"]:

        decision = (

            "Reject the null hypothesis."

        )

    else:

        decision = (

            "Fail to reject the null hypothesis."

        )

    return {

        "Statistic":

        result["Statistic"],

        "p-value":

        result["p-value"],

        "Decision":

        decision

          }


def mann_whitney(
        group1,
        group2,
        alpha=0.05):

    """
    Mann-Whitney U Test.
    """

    statistic, p = mannwhitneyu(
        group1,
        group2,
        alternative="two-sided"
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": p < alpha

    }

def wilcoxon_signed_rank(
        before,
        after,
        alpha=0.05):

    """
    Wilcoxon Signed-Rank Test.
    """

    statistic, p = wilcoxon(
        before,
        after
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": p < alpha

    }

def kruskal_wallis(
        *groups,
        alpha=0.05):

    """
    Kruskal-Wallis H Test.
    """

    statistic, p = kruskal(
        *groups
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": p < alpha

    }

def friedman(
        *groups,
        alpha=0.05):

    """
    Friedman Test.
    """

    statistic, p = friedmanchisquare(
        *groups
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": p < alpha

    }

def median_test_groups(
        *groups,
        alpha=0.05):

    """
    Mood Median Test.
    """

    statistic, p, median, table = median_test(
        *groups
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Median": float(median),

        "Reject H0": p < alpha

    }

def mood_test(
        group1,
        group2,
        alpha=0.05):

    """
    Mood's Test for Scale.
    """

    statistic, p = mood(
        group1,
        group2
    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p),

        "Reject H0": p < alpha

    }

def rank_biserial(
        group1,
        group2):

    """
    Rank-biserial correlation.
    """

    u, _ = mannwhitneyu(
        group1,
        group2
    )

    n1 = len(group1)

    n2 = len(group2)

    return 1 - (

        2 * u

    ) / (

        n1 * n2

    )

def sign_test(
        before,
        after):

    """
    Simple Sign Test.
    """

    before = np.asarray(before)

    after = np.asarray(after)

    positive = np.sum(after > before)

    negative = np.sum(after < before)

    ties = np.sum(after == before)

    return {

        "Positive": int(positive),

        "Negative": int(negative),

        "Ties": int(ties)

    }


def permutation_pvalue(
        observed,
        permutations):

    """
    Empirical permutation p-value.
    """

    permutations = np.asarray(
        permutations
    )

    return np.mean(

        permutations >= observed

    )

def bootstrap_mean(
        values,
        n_bootstrap=1000):

    """
    Bootstrap estimate of mean.
    """

    values = np.asarray(values)

    means = []

    for _ in range(n_bootstrap):

        sample = np.random.choice(

            values,

            size=len(values),

            replace=True

        )

        means.append(

            np.mean(sample)

        )

    return {

        "Mean":

        float(np.mean(means)),

        "Std":

        float(np.std(means))

    }

def cohens_d(
        group1,
        group2):

    """
    Cohen's d effect size.
    """

    group1 = np.asarray(group1)
    group2 = np.asarray(group2)

    n1 = len(group1)
    n2 = len(group2)

    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)

    pooled = np.sqrt(

        ((n1 - 1) * var1 +
         (n2 - 1) * var2)

        /

        (n1 + n2 - 2)

    )

    return (

        np.mean(group1)

        -

        np.mean(group2)

    ) / pooled

  def hedges_g(
        group1,
        group2):

    """
    Hedges' g.
    """

    d = cohens_d(
        group1,
        group2
    )

    n = len(group1) + len(group2)

    correction = 1 - (

        3 /

        (4 * n - 9)

    )

    return d * correction
def glass_delta(
        treatment,
        control):

    """
    Glass's Delta.
    """

    return (

        np.mean(treatment)

        -

        np.mean(control)

    ) / np.std(
        control,
        ddof=1
    )

def cliffs_delta(
        group1,
        group2):

    """
    Cliff's Delta.
    """

    greater = 0
    lower = 0

    for x in group1:

        for y in group2:

            if x > y:
                greater += 1

            elif x < y:
                lower += 1

    return (

        greater -

        lower

    ) / (

        len(group1)

        *

        len(group2)

          )

def eta_squared(
        ss_between,
        ss_total):

    """
    Eta squared.
    """

    return ss_between / ss_total

def omega_squared(
        ss_between,
        ss_total,
        df_between,
        ms_error):

    """
    Omega squared.
    """

    numerator = (

        ss_between

        -

        df_between * ms_error

    )

    denominator = (

        ss_total

        +

        ms_error

    )

    return numerator / denominator

def epsilon_squared(
        h,
        n,
        k):

    """
    Epsilon squared
    for Kruskal-Wallis.
    """

    return (

        h

        -

        k

        +

        1

    ) / (

        n

        -

        k

    )

def epsilon_squared(
        h,
        n,
        k):

    """
    Epsilon squared
    for Kruskal-Wallis.
    """

    return (

        h

        -

        k

        +

        1

    ) / (

        n

        -

        k

          )

def common_language_effect(
        group1,
        group2):

    """
    Probability that a randomly
    selected observation from
    group1 exceeds one from group2.
    """

    wins = 0

    total = 0

    for x in group1:

        for y in group2:

            total += 1

            if x > y:

                wins += 1

    return wins / total

def rank_effect(
        group1,
        group2):

    """
    Rank-based effect size.
    """

    return rank_biserial(
        group1,
        group2
    )

def interpret_effect_size(
        value):

    """
    Cohen interpretation.
    """

    value = abs(value)

    if value < 0.20:

        return "Negligible"

    elif value < 0.50:

        return "Small"

    elif value < 0.80:

        return "Medium"

    return "Large"

def bonferroni_correction(
        p_values,
        alpha=0.05):

    """
    Bonferroni multiple testing correction.
    """

    reject, corrected, _, _ = multipletests(
        p_values,
        alpha=alpha,
        method="bonferroni"
    )

    return {

        "Corrected p-values": corrected,

        "Reject": reject

    }

def holm_correction(
        p_values,
        alpha=0.05):

    """
    Holm-Bonferroni correction.
    """

    reject, corrected, _, _ = multipletests(

        p_values,

        alpha=alpha,

        method="holm"

    )

    return {

        "Corrected p-values": corrected,

        "Reject": reject

          }

def sidak_correction(
        p_values,
        alpha=0.05):

    """
    Sidak correction.
    """

    reject, corrected, _, _ = multipletests(

        p_values,

        alpha=alpha,

        method="sidak"

    )

    return {

        "Corrected p-values": corrected,

        "Reject": reject

    }

def benjamini_hochberg(
        p_values,
        alpha=0.05):

    """
    False Discovery Rate correction.
    """

    reject, corrected, _, _ = multipletests(

        p_values,

        alpha=alpha,

        method="fdr_bh"

    )

    return {

        "Corrected p-values": corrected,

        "Reject": reject

          }

def benjamini_yekutieli(
        p_values,
        alpha=0.05):

    """
    FDR under dependency.
    """

    reject, corrected, _, _ = multipletests(

        p_values,

        alpha=alpha,

        method="fdr_by"

    )

    return {

        "Corrected p-values": corrected,

        "Reject": reject

    }

def tukey_hsd(
        values,
        groups):

    """
    Tukey Honest Significant Difference.
    """

    result = pairwise_tukeyhsd(

        endog=values,

        groups=groups,

        alpha=0.05

    )

    return result

def pairwise_matrix(
        dataframe):

    """
    Pairwise p-value matrix.
    """

    cols = dataframe.columns

    matrix = pd.DataFrame(

        np.ones(

            (len(cols),
             len(cols))

        ),

        index=cols,

        columns=cols

    )

    for i in range(len(cols)):

        for j in range(i + 1, len(cols)):

            _, p = ttest_ind(

                dataframe.iloc[:, i],

                dataframe.iloc[:, j]

            )

            matrix.iloc[i, j] = p

            matrix.iloc[j, i] = p

    return matrix

def significance_stars(
        p):

    """
    Convert p-values into
    publication symbols.
    """

    if p < 0.0001:
        return "****"

    elif p < 0.001:
        return "***"

    elif p < 0.01:
        return "**"

    elif p < 0.05:
        return "*"

    return "ns"

def significance_table(
        p_values):

    """
    Summary table.
    """

    return pd.DataFrame({

        "p-value":

        p_values,

        "Significance":

        [

            significance_stars(p)

            for p in p_values

        ]

    })

def statistical_report(
        p_value,
        effect_size=None):

    """
    Publication-ready summary.
    """

    report = {

        "p-value": p_value,

        "Significant": p_value < 0.05,

        "Stars":

        significance_stars(

            p_value

        )

    }

    if effect_size is not None:

        report["Effect Size"] = effect_size

        report["Interpretation"] = \

            interpret_effect_size(

                effect_size

            )

    return report

def pearson(
        x,
        y):

    """
    Pearson correlation coefficient.
    """

    r, p = pearsonr(x, y)

    return {

        "Correlation": float(r),

        "p-value": float(p),

        "Strength": correlation_strength(r)

    }

def spearman(
        x,
        y):

    """
    Spearman rank correlation.
    """

    r, p = spearmanr(x, y)

    return {

        "Correlation": float(r),

        "p-value": float(p),

        "Strength": correlation_strength(r)

              }

def kendall_tau(
        x,
        y):

    """
    Kendall Tau correlation.
    """

    r, p = kendalltau(x, y)

    return {

        "Correlation": float(r),

        "p-value": float(p),

        "Strength": correlation_strength(r)

    }

def point_biserial(
        binary,
        continuous):

    """
    Point biserial correlation.
    """

    r, p = pointbiserialr(
        binary,
        continuous
    )

    return {

        "Correlation": float(r),

        "p-value": float(p)

    }

def phi_coefficient(
        contingency):

    """
    Phi coefficient for 2x2 tables.
    """

    chi2, _, _, _ = chi2_contingency(
        contingency
    )

    n = contingency.sum()

    return np.sqrt(
        chi2 / n
    )

def cramers_v(
        contingency):

    """
    Cramer's V.
    """

    chi2, _, _, _ = chi2_contingency(
        contingency
    )

    n = contingency.sum()

    r, c = contingency.shape

    return np.sqrt(

        chi2 /

        (

            n *

            (min(r - 1,
                 c - 1))

        )

    )

def correlation_matrix(
        dataframe,
        method="pearson"):

    """
    Correlation matrix.
    """

    return dataframe.corr(
        method=method
          )


def covariance_matrix(
        dataframe):

    """
    Covariance matrix.
    """

    return dataframe.cov()

def partial_correlation(
        dataframe):

    """
    Partial correlation matrix.
    """

    cov = dataframe.cov()

    precision = pinv(cov)

    d = np.sqrt(
        np.diag(precision)
    )

    partial = -precision / np.outer(
        d,
        d
    )

    np.fill_diagonal(
        partial,
        1
    )

    return pd.DataFrame(

        partial,

        columns=dataframe.columns,

        index=dataframe.columns

          )

def distance_correlation(
        x,
        y):

    """
    Distance correlation.
    """

    x = np.asarray(x)

    y = np.asarray(y)

    a = squareform(
        pdist(
            x[:, None]
        )
    )

    b = squareform(
        pdist(
            y[:, None]
        )
    )

    A = a - a.mean(axis=0) \
          - a.mean(axis=1)[:,None] \
          + a.mean()

    B = b - b.mean(axis=0) \
          - b.mean(axis=1)[:,None] \
          + b.mean()

    dcov = np.sqrt(

        np.mean(A * B)

    )

    dvarx = np.sqrt(

        np.mean(A * A)

    )

    dvary = np.sqrt(

        np.mean(B * B)

    )

    return dcov / np.sqrt(

        dvarx *

        dvary

    )

def correlation_strength(r):

    """
    Interpret correlation.
    """

    r = abs(r)

    if r < 0.20:

        return "Very Weak"

    elif r < 0.40:

        return "Weak"

    elif r < 0.60:

        return "Moderate"

    elif r < 0.80:

        return "Strong"

    return "Very Strong"

def correlation_report(
        x,
        y):

    """
    Complete report.
    """

    return {

        "Pearson":

        pearson(
            x,
            y
        ),

        "Spearman":

        spearman(
            x,
            y
        ),

        "Kendall":

        kendall_tau(
            x,
            y
        )

    }

from scipy.stats import shapiro

def choose_test(*groups, paired=False, alpha=0.05):
    """
    Automatically recommend an appropriate statistical test.

    Parameters
    ----------
    *groups : array-like
        Two or more groups of observations.
    paired : bool
        Whether the samples are paired.
    alpha : float
        Significance level.

    Returns
    -------
    dict
        Recommended statistical test and reasoning.
    """

    groups = [np.asarray(g) for g in groups]

    normal = all(shapiro(g).pvalue > alpha for g in groups)

    if len(groups) == 2:

        if paired:

            test = (
                "paired_ttest"
                if normal
                else "wilcoxon_signed_rank"
            )

        else:

            variance = levene_test(*groups)

            equal = variance["Equal Variance"]

            if normal:

                test = (
                    "independent_ttest"
                    if equal
                    else "welch_ttest"
                )

            else:

                test = "mann_whitney"

    else:

        if normal:

            test = "one_way_anova"

        else:

            test = "kruskal_wallis"

    return {

        "Recommended Test": test,

        "Normal": normal,

        "Number of Groups": len(groups)

          }

def recommend_effect_size(test_name):

    """
    Suggest an appropriate effect size
    for a statistical test.
    """

    mapping = {

        "independent_ttest": "cohens_d",

        "paired_ttest": "cohens_d",

        "welch_ttest": "hedges_g",

        "mann_whitney": "cliffs_delta",

        "kruskal_wallis": "epsilon_squared",

        "one_way_anova": "eta_squared",

        "friedman": "kendalls_w"

    }

    return mapping.get(

        test_name,

        "None"

    )

def compare_models(
        dataframe,
        alpha=0.05):

    """
    Automatically compare all
    models contained in a dataframe.
    """

    report = {}

    columns = dataframe.columns

    for i in range(len(columns)):

        for j in range(i + 1, len(columns)):

            a = dataframe.iloc[:, i]

            b = dataframe.iloc[:, j]

            recommendation = choose_test(

                a,

                b,

                alpha=alpha

            )

            report[

                f"{columns[i]} vs {columns[j]}"

            ] = recommendation

    return report

def benchmark_report(results):

    """
    Produce a benchmark summary.
    """

    report = {

        "Best":

        max(results,
            key=results.get),

        "Worst":

        min(results,
            key=results.get),

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

    return report




    
