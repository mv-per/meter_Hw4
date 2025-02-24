from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from numpy.typing import NDArray
# Importing the parent: DataPreprocessing class from data_preprocess.py
from meter.data_preprocess import DataPreprocessing 


class ModelBuilder(DataPreprocessing):


    def __init__(self, *args, **kwargs):
        super(ModelBuilder, self).__init__(*args, **kwargs)


    def split_dataset(self, X, y):
        from sklearn.model_selection import train_test_split
        X_train_validation, X_test, y_train_validation, y_test = train_test_split(X,y, test_size = 0.2, random_state=12)

        X_train, X_validation, y_train, y_validation = train_test_split(X_train_validation,y_train_validation, test_size = 0.2, random_state=99)

        # Sanity check
        assert X_test.shape[0] == y_test.shape[0]
        assert X_train.shape[0] == y_train.shape[0]
        assert X_validation.shape[0] == y_validation.shape[0]

        return (X_train, X_test, X_validation), (y_train, y_test, y_validation)


    def dt(self, X_train, X_test, y_train, y_test):
        #Create DT model
        DT_classifier = DecisionTreeClassifier()

        #Train the model
        DT_classifier.fit(X_train, y_train)

        #Test the model
        DT_predicted = DT_classifier.predict(X_test)

        error = 0
        for i in range(len(y_test)):
            error += np.sum(DT_predicted != y_test)

        # total_accuracy = 1 - error / len(y_test)

        #get performance
        self.accuracy = accuracy_score(y_test, DT_predicted)

        return DT_classifier