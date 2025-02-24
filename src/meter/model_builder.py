from sklearn.tree import DecisionTreeClassifier
import numpy as np



class ModelBuilder():


    def split_dataset(self, X, y):
        from sklearn.model_selection import train_test_split
        X_train_validation, X_test, y_train_validation, y_test = train_test_split(X,y, test_size = 0.2, random_state=12)

        X_train, X_validation, y_train, y_validation = train_test_split(X_train_validation,y_train_validation, test_size = 0.2, random_state=99)

        # Sanity check
        assert X_test.shape[0] == y_test.shape[0]
        assert X_train.shape[0] == y_train.shape[0]
        assert X_validation.shape[0] == y_validation.shape[0]

        return (X_train, X_test, X_validation), (y_train, y_test, y_validation)


    def _get_accuracy(self,ytrue, y_predicted) -> None:
        from sklearn.metrics import accuracy_score
        self.accuracy = accuracy_score(ytrue, y_predicted)

    def fit_classifier(self,X_train, y_train ) -> DecisionTreeClassifier:
        classifier = DecisionTreeClassifier()
        classifier.fit(X_train, y_train)
        return classifier

    def classify(self, X_train, X_test, y_train, y_test):
        #Create DT model
        

        #Train the model
        classifier= self.fit_classifier(X_train, y_train)

        #Test the model
        y_predicted = classifier.predict(X_test)

        error = 0
        for i in range(len(y_test)):
            error += np.sum(y_predicted != y_test)

        # total_accuracy = 1 - error / len(y_test)

        #get performance
        self._get_accuracy(y_test, y_predicted)

        return classifier