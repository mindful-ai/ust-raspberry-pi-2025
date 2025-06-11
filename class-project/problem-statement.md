# 🧠 Assessment Project: Real-Time Handwritten Character Recognition using TensorFlow Lite on Raspberry Pi

## 🎯 Objective

Build and deploy a machine learning model that recognizes handwritten characters (A–Z) using a webcam connected to Raspberry Pi. The project should use TensorFlow Lite to ensure the model is lightweight and efficient.

---

## 📦 Requirements

### Model Training (on Laptop)
- Use `EMNIST Letters` dataset.
- Train a CNN model with 26 output classes (A–Z).
- Export trained model as `.tflite`.

### Deployment (on Raspberry Pi)
- Transfer the model to Raspberry Pi.
- Use a webcam to capture character input.
- Preprocess input (resize to 28x28 grayscale).
- Perform prediction using `tflite-runtime`.
- Display output character and confidence score.

---

## ✅ Deliverables

- `model.tflite` — Trained and converted model.
- `train_model.ipynb` — Training notebook.
- `inference.py` — Raspberry Pi inference script.
- `README.md` — Setup and usage guide.
- (Optional) `log.csv` — Prediction logs.

---

## 🕵️ Evaluation Criteria

| Criteria                         | Marks |
|----------------------------------|-------|
| Model accuracy ≥ 85%             | 20    |
| Model successfully converted     | 20    |
| Real-time prediction on Pi       | 30    |
| Code quality and modularity      | 20    |
| Optional features (logs/UI)      | 10    |

---

## 📬 Notes

- Model must run in < 1 second per inference.
- Consider using quantization to reduce model size.
- Use `cv2.imshow` to display predictions in webcam feed.


# 🧾 Reference Answer Key: Character Recognition with TensorFlow Lite

## ✅ Model Architecture

- Use `tensorflow.keras` to define a CNN:
```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(26, activation='softmax')
])
```

### Model Conversion

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Quantization (optional)
tflite_model = converter.convert()
with open("model.tflite", "wb") as f:
    f.write(tflite_model)

import tflite_runtime.interpreter as tflite
import cv2, numpy as np

interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

```

### 🖥️ Inference Script Highlights

```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    roi = preprocess(frame)  # 28x28 grayscale
    interpreter.set_tensor(input_details[0]['index'], roi)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    pred = chr(np.argmax(output) + 65)
    cv2.putText(frame, f'Pred: {pred}', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow("Live", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### ✅ Notes

Install requirements on Pi:

sudo apt install libatlas-base-dev
pip3 install numpy opencv-python tflite-runtime

You can draw characters on paper and show to the webcam for testing.

Tweak image preprocessing if needed (blur, thresholding, etc.).

