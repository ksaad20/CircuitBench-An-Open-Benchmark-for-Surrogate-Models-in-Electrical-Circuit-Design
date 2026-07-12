"""
Dataset Integrity Checks
"""

import pandas as pd


class DatasetIntegrity:
    @staticmethod
    def duplicate_rows(df: pd.DataFrame):

        return int(df.duplicated().sum())

    @staticmethod
    def missing_values(df: pd.DataFrame):

        return df.isnull().sum()

    @staticmethod
    def total_missing(df: pd.DataFrame):

        return int(df.isnull().sum().sum())

    @staticmethod
    def shape(df: pd.DataFrame):

        return df.shape

    @staticmethod
    def memory_usage(df: pd.DataFrame):

        return int(df.memory_usage(deep=True).sum())

    @staticmethod
    def report(df: pd.DataFrame):

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "duplicates": DatasetIntegrity.duplicate_rows(df),
            "total_missing": DatasetIntegrity.total_missing(df),
            "memory_bytes": DatasetIntegrity.memory_usage(df),
        }
