"""
Dataset Splitting Utilities
"""

from sklearn.model_selection import train_test_split


class TrainTestSplitter:

    def __init__(
        self,
        test_size=0.2,
        random_state=42,
        shuffle=True
    ):

        self.test_size = test_size
        self.random_state = random_state
        self.shuffle = shuffle

    def split(self, X, y=None):

        if y is None:

            return train_test_split(
                X,
                test_size=self.test_size,
                random_state=self.random_state,
                shuffle=self.shuffle
            )

        return train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            shuffle=self.shuffle
        )
