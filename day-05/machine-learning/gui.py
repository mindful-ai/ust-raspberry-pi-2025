# gui.py
import tkinter as tk
from ml_logic import IrisModel

class IrisGUI:
    def __init__(self, root):
        self.model = IrisModel()
        self.root = root
        self.root.title("Iris Species Predictor")

        tk.Label(root, text="Train & Predict on Iris Dataset", font=("Arial", 16, "bold")).pack(pady=10)

        # Train button
        self.train_button = tk.Button(root, text="Train and Save Model", command=self.train_model)
        self.train_button.pack(pady=5)

        # Accuracy display
        self.accuracy_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.accuracy_label.pack(pady=5)

        # Input fields for features
        self.entries = []
        self.feature_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

        for feature in self.feature_names:
            frame = tk.Frame(root)
            frame.pack(pady=2)
            tk.Label(frame, text=f"{feature}:", width=15, anchor='e').pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.entries.append(entry)

        # Predict button
        self.predict_button = tk.Button(root, text="Predict Species", command=self.predict_species)
        self.predict_button.pack(pady=10)

        # Prediction result
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
        self.result_label.pack(pady=10)

    def train_model(self):
        accuracy = self.model.train_and_save_model()
        self.accuracy_label.config(text=f"Model trained and saved. Accuracy: {accuracy*100:.2f}%")

    def predict_species(self):
        try:
            features = [float(entry.get()) for entry in self.entries]
            prediction = self.model.predict(features)
            self.result_label.config(text=f"Predicted Species: {prediction}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers for all fields.", fg="red")
