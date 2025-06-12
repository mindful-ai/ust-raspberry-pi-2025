# 🧠 Object Detection on Raspberry Pi using EfficientDet-Lite0 (TFLite)

## 📌 Overview

This project demonstrates how to use the **EfficientDet-Lite0 TensorFlow Lite model** for **real-time object detection** on edge devices such as Raspberry Pi.

EfficientDet-Lite0 is:
- Pre-trained on the **COCO dataset (90 classes)**
- Optimized for **speed and efficiency**
- Compact in size (~4.4MB)
- Ideal for **low-latency inference** on embedded systems

---

## 📦 Model

**Model:** `efficientdet_lite0.tflite`  
**Source:** [TensorFlow Model Zoo](https://www.tensorflow.org/lite/models/object_detection/overview)

Download:
```bash
wget https://github.com/schu-lab/Tensorflow-Object-Detection/raw/main/efficientdet_lite0.tflite
```

---

## ⚙️ Requirements (on Raspberry Pi)

```bash
sudo apt update
sudo apt install libatlas-base-dev
pip3 install tflite-runtime numpy opencv-python
```

---

## 📷 Sample Python Code (`object_detection.py`)

```python
import tflite_runtime.interpreter as tflite
import numpy as np
import cv2

# Load TFLite model
interpreter = tflite.Interpreter(model_path="efficientdet_lite0.tflite")
interpreter.allocate_tensors()

# Get input/output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize input to model's expected size (320x320)
    input_shape = input_details[0]['shape']
    input_data = cv2.resize(frame, (input_shape[2], input_shape[1]))
    input_data = np.expand_dims(input_data, axis=0).astype(np.uint8)

    # Inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Get results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]      # Bounding boxes
    classes = interpreter.get_tensor(output_details[1]['index'])[0]    # Class indices
    scores = interpreter.get_tensor(output_details[2]['index'])[0]     # Confidence scores

    height, width, _ = frame.shape
    for i in range(len(scores)):
        if scores[i] > 0.5:
            ymin, xmin, ymax, xmax = boxes[i]
            (left, top, right, bottom) = (int(xmin * width), int(ymin * height),
                                          int(xmax * width), int(ymax * height))
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"Class {int(classes[i])} ({int(scores[i]*100)}%)",
                        (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255), 1)

    cv2.imshow('EfficientDet Lite0 - Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🧠 Notes

- The model detects objects from the **COCO dataset (90 common objects)**.
- Class labels can be mapped using the [COCO label file](https://github.com/amikelive/coco-labels/blob/master/coco-labels-paper.txt).
- For better performance, ensure lighting is good and background is uncluttered.
- Consider quantization-aware conversion for further optimization.

---

## 📊 Advantages of EfficientDet-Lite0

| Feature            | Benefit                                |
|--------------------|-----------------------------------------|
| Small Size         | ~4.4 MB                                |
| Fast Inference     | <100ms/frame on Raspberry Pi 4         |
| Real-time capable  | Yes                                    |
| Pretrained         | 90 COCO classes                        |
| Easy to use        | Compatible with `tflite_runtime`       |

---

## ✅ Summary

EfficientDet-Lite0 is a powerful, lightweight object detection model well-suited for edge computing. With minimal setup, you can build real-time detection applications using a Raspberry Pi and a webcam.
