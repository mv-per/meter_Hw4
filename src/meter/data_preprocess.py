import pandas as pd


class DataPreprocessing():
    def __init__(self):
        pass

    def load_data(self, path):
        data = pd.read_csv(path, sep="\t", header=None).dropna()

        print(data.head())

        data = data.to_numpy()

        return self.normalize_data(data)
    
    def normalize_data(self, data):
        from sklearn.preprocessing import StandardScaler

        print("normalizing dataset")

        return StandardScaler().fit_transform(data)