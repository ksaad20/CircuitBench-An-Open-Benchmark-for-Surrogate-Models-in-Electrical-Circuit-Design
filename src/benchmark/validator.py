"""
Validation utilities.
"""

import numpy as np


class Validator:

    @staticmethod
    def check_length(a,b):

        if len(a)!=len(b):

            raise ValueError(
                "Prediction length mismatch."
            )

    @staticmethod
    def check_nan(x):

        if np.isnan(x).any():

            raise ValueError(
                "NaN values detected."
            )
