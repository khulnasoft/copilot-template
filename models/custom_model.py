from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class CustomModel(BaseEstimator, ClassifierMixin):
    def __init__(self, param1=1, param2=2):
        self.param1 = param1
        self.param2 = param2

    def fit(self, X, y):
        # Custom training logic
        self.classes_ = np.unique(y)
        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):
        # Custom prediction logic
        return np.random.choice(self.classes_, len(X))

    def predict_proba(self, X):
        # Custom probability prediction logic
        return np.ones((len(X), len(self.classes_))) / len(self.classes_)
