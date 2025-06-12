# Train and Deploy a Machine Learning Model on Raspberry Pi

## 📝 Project: Iris Species Classifier

This project demonstrates how to train a machine learning model on your **laptop** and deploy it to a **Raspberry Pi** for inference.

---

## 💻 Part 1: Train on Laptop

### 🔹 Code: `train_model.py`

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Save model
joblib.dump(model, 'iris_model.joblib')
```

### 📁 Part 2: Transfer Model to Raspberry Pi

scp iris_model.joblib pi@<raspberry-pi-ip>:/home/pi/


### 🧪 Part 3: Inference on Raspberry Pi

#### Option A: Command Line

```python
import joblib
import numpy as np

# Load model
model = joblib.load('iris_model.joblib')

# Take input
features = input("Enter 4 features (comma separated): ")
features = np.array([float(x) for x in features.split(',')]).reshape(1, -1)

# Predict
pred = model.predict(features)
print(f"Predicted class: {pred[0]}")


```

RUN: python3 predict.py


#### 🔸 Option B: Flask Web API

pip3 install flask joblib


```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('iris_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    prediction = model.predict([data]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


```

RUN: python3 app.py
RUN: curl -X POST http://<pi-ip>:5000/predict -H "Content-Type: application/json" -d '{"features":[5.1,3.5,1.4,0.2]}'

### 📌 Summary

| Task                   | On Laptop           | On Raspberry Pi               |
| ---------------------- | ------------------- | ----------------------------- |
| Train Model            | `train_model.py`    | ❌                             |
| Save Model             | `iris_model.joblib` | Used for inference            |
| Transfer Model         | `scp`               | `iris_model.joblib` goes here |
| Inference (CLI or API) | ❌                   | `predict.py` or `app.py`      |
