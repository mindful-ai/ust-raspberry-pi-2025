
# Deploying Machine Learning Models on Raspberry Pi with TensorFlow Lite

## 🚀 1. What is TensorFlow Lite?

**TensorFlow Lite** is a lightweight, fast runtime for running TensorFlow models on **edge devices**, such as:

- Raspberry Pi
- Android devices
- Microcontrollers (with TinyML)

### 🔧 Key Features

| Feature                  | Benefit                          |
|--------------------------|----------------------------------|
| Model quantization       | Smaller, faster models           |
| Edge device compatibility| Run on Pi, phones, microcontrollers |
| Low latency inference    | Ideal for real-time predictions  |
| No need for GPU          | Optimized for CPU & EdgeTPU      |

---

## 🔧 2. What is TensorRT?

**TensorRT** is **NVIDIA's high-performance deep learning inference library**. It’s not used directly with Raspberry Pi (unless using Jetson Nano).

| Tool              | Best For                      | Supported Hardware |
|-------------------|-------------------------------|--------------------|
| TensorFlow Lite   | Raspberry Pi, ARM devices     | CPU, Coral EdgeTPU |
| TensorRT          | Jetson Nano, NVIDIA GPUs      | NVIDIA GPUs        |

---

## 🍓 3. Why Use TensorFlow Lite on Raspberry Pi?

Because full TensorFlow is too large and heavy for Pi. TFLite models:

- Load faster
- Require less memory
- Inference is faster
- Run without GPU

---

## 🛠️ 4. How to Use TensorFlow Lite on Raspberry Pi

### Step-by-Step Demo: Image Classification

### (A) Convert Your Model to `.tflite` Format (on Laptop)

```
import tensorflow as tf

model = tf.keras.models.load_model('mymodel.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

### (B) Transfer Model to Raspberry Pi

```bash
scp model.tflite pi@<raspberry-pi-ip>:/home/pi/
```

### (C) Run Inference on Raspberry Pi

```bash
pip3 install tflite-runtime
```

```python
import numpy as np
import tflite_runtime.interpreter as tflite

interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_data = np.array(np.random.random_sample(input_details[0]['shape']), dtype=np.float32)

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
print("Prediction:", output_data)
```

---

## 🧠 5. Advanced: Add Coral Edge TPU for Speed

- TensorFlow Lite works with **Google Coral USB Accelerator**
- You can quantize model and compile it using Edge TPU compiler
- Speeds up inference **10–50x**

---

## ✅ Summary

| Topic             | Details                                   |
|------------------|--------------------------------------------|
| TensorFlow Lite  | Lightweight runtime for ML on edge devices |
| Use on Pi        | Smaller model, faster prediction           |
| Tools needed     | `tflite-runtime`, pre-converted model      |
| Optional         | Coral Edge TPU for ultra-fast inference    |
