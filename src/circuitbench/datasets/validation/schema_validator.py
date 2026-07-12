"""
Dataset Schema Validator
"""

import pandas as pd


class SchemaValidator:

    def __init__(self):

        self.required_columns = []

    def require(self, columns):

        self.required_columns = list(columns)

    def validate(self, dataframe: pd.DataFrame):

        missing = []

        for column in self.required_columns:

            if column not in dataframe.columns:

                missing.append(column)

        return {
            "valid": len(missing) == 0,
            "missing_columns": missing,
            "n_columns": len(dataframe.columns),
            "columns": list(dataframe.columns),
        }

    def validate_target(self, dataframe, target):

        return target in dataframe.columns
