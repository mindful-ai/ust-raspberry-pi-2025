# ❤️ Assessment Problem: Heart Disease Prediction using Tkinter GUI

## 🎯 Objective

Design and implement a **Tkinter-based GUI application** to predict the presence of **heart disease** using a **machine learning model** trained on a provided dataset. This project must demonstrate a clear **separation of concerns**:  
- **Model logic** (data processing, training, prediction)  
- **GUI logic** (user interface and input/output display)  
- **Main script** to integrate both

---

## 🩺 Dataset

You will be provided with a cleaned heart disease dataset (`heart.csv`) containing the following features:

- `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`  
- Target variable: `target` (1 = heart disease present, 0 = not present)

---

## 📁 Project Structure

heart_disease_predictor/ <br>
├── model_logic.py # Machine learning pipeline and prediction logic <br>
├── gui.py # Tkinter GUI code <br>
├── main.py # Integrates model and GUI <br>
├── heart.csv # Dataset file <br>
└── README.md # Instructions to run the project <br>


---

## 🧠 Functional Requirements

### 1. Model Logic (`model_logic.py`)
- Load the dataset and preprocess it (if necessary).
- Train a classifier (e.g., Logistic Regression, Random Forest).
- Save the model using `joblib` or `pickle`.
- Provide a `predict(input_dict)` function that:
  - Takes a dictionary of user inputs.
  - Returns the prediction (0 or 1) and confidence.

### 2. GUI (`gui.py`)
- Use **Tkinter** to build a user-friendly form.
- Form must accept inputs for each feature required for prediction.
- Include:
  - Labels and Entry/Dropdown widgets for each feature.
  - A “Predict” button that triggers the model.
  - A “Reset” button to clear inputs.
  - A label or textbox to display the prediction result.
- No logic/model code should exist in this file.

### 3. Integration (`main.py`)
- Import the GUI and model modules.
- Hook up the GUI form to call `predict()` on button click.
- Display the result in the GUI window.

---

## ✅ Evaluation Criteria

| Criteria                          | Weightage |
|----------------------------------|-----------|
| Functional model training & prediction | 25% |
| Tkinter GUI usability and responsiveness | 25% |
| Clear modularization of logic and GUI   | 20% |
| Code readability, comments, structure   | 15% |
| Bonus features (graph, history, feedback) | 15% |

---

## 🎁 Bonus Features (Optional)
- Plot prediction probabilities using `matplotlib`.
- Save and show prediction history in the UI.
- Add validation to ensure all inputs are numeric or valid.
- Allow users to reload a trained model without retraining.

---

## 🚀 Submission

Submit a `.zip` file or GitHub repository containing:
- All `.py` files (`model_logic.py`, `gui.py`, `main.py`)
- `heart.csv` dataset
- `README.md` with:
  - Setup instructions
  - How to run the app
  - Optional: Screenshots of the UI

---

## 💡 Tips

- Use `scikit-learn` for the model.
- Use `joblib.dump()` and `joblib.load()` for saving/loading.
- Use `.grid()` or `.pack()` for GUI layout.
- For dropdowns, use `tk.OptionMenu` or `ttk.Combobox`.

---

## 📝 Sample Prediction Fields (GUI)

| Field      | Widget Type   |
|------------|---------------|
| Age        | Entry         |
| Sex        | Dropdown (0/1)|
| Chest Pain | Dropdown (0–3)|
| Cholesterol| Entry         |
| ...        | ...           |

---

## 📌 End Goal

A fully functional app that can take patient details as input, predict the likelihood of heart disease, and present the result cleanly in a GUI.

---

Good luck and build with heart! ❤️
