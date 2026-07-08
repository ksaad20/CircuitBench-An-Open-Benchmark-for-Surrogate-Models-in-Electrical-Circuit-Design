"""
Hypothesis testing.
"""

from scipy.stats import ttest_rel

from scipy.stats import ttest_ind

from scipy.stats import wilcoxon

from scipy.stats import friedmanchisquare


class HypothesisTest:

    @staticmethod
    def paired_t(a, b):

        statistic, p = ttest_rel(a, b)

        return {

            "test": "paired_t",

            "statistic": statistic,

            "p_value": p

        }

    @staticmethod
    def independent_t(a, b):

        statistic, p = ttest_ind(

            a,

            b,

            equal_var=False

        )

        return {

            "test": "independent_t",

            "statistic": statistic,

            "p_value": p

        }

    @staticmethod
    def wilcoxon(a, b):

        statistic, p = wilcoxon(a, b)

        return {

            "test": "wilcoxon",

            "statistic": statistic,

            "p_value": p

        }

    @staticmethod
    def friedman(*groups):

        statistic, p = friedmanchisquare(*groups)

        return {

            "test": "friedman",

            "statistic": statistic,

            "p_value": p

        }
