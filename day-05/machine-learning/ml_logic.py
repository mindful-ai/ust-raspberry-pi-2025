# ml_logic.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class IrisModel:
    def __init__(self):
        self.model = None
        self.target_names = None
        self.model_path = "iris_model.pkl"

    def train_and_save_model(self):
        iris = load_iris()
        X = iris.data
        y = iris.target
        self.target_names = iris.target_names

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        joblib.dump((clf, iris.target_names), self.model_path)

        return clf.score(X_test, y_test)

    def load_model(self):
        clf, target_names = joblib.load(self.model_path)
        self.model = clf
        self.target_names = target_names

    def predict(self, features):
        if self.model is None:
            self.load_model()
        prediction = self.model.predict([features])
        return self.target_names[prediction[0]]
