import numpy as np
import pandas as pd


class DataPreprocessing:
    def __init__(self):
        pass

    def load_data(self, path, y_column: int | None = None):
        data = pd.read_csv(path, sep="\t", header=None).dropna()
        y = None
        print(data.head())

        data = data.to_numpy()

        if y_column is not None:
            y = data[:, y_column]
            data = np.delete(data, [y_column], axis=1)

        data = self.normalize_data(data)

        return data, y

    def normalize_data(self, data):
        from sklearn.preprocessing import StandardScaler

        print("normalizing dataset")

        return StandardScaler().fit_transform(data)
