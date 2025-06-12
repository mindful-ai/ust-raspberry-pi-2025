
# TensorFlow Lite Object Detection on Raspberry Pi using Webcam

This project demonstrates how to run real-time object detection on a Raspberry Pi using a pre-trained TensorFlow Lite model and a USB webcam.

---

## 🧰 Requirements

### Hardware
- Raspberry Pi 3 or 4
- USB Webcam (e.g., Logitech C270 or similar)
- MicroSD card with Raspberry Pi OS
- Internet connectivity (to install packages)

### Software
- Python 3.7+
- Packages:
    ```bash
    pip3 install opencv-python tflite-runtime numpy
    ```

---

## 📁 Project Files

| File           | Description                                      |
|----------------|--------------------------------------------------|
| `detect.py`    | Main Python script for object detection          |
| `labelmap.txt` | List of labels for detected objects              |
| `model.tflite` | Pre-trained TensorFlow Lite model (add manually) |
| `README.md`    | Project instructions and setup                   |

---

## 🧠 Step-by-Step Setup

### 1. Install Dependencies on Raspberry Pi

```bash
sudo apt update
sudo apt install python3-pip
pip3 install opencv-python tflite-runtime numpy
```

### 2. Download a Pre-trained TFLite Model

Download from [TensorFlow Lite Model Zoo](https://www.tensorflow.org/lite/models/object_detection/overview). Example:

Alternative: https://github.com/schu-lab/Tensorflow-Object-Detection/blob/main/efficientdet_lite0.tflite



- EfficientDet Lite0:
    - File: `efficientdet_lite0.tflite`
    - Rename it to `model.tflite`

### 3. Transfer Project Files to Raspberry Pi

If working on another machine, transfer files:

```bash
scp -r tflite_rpi_webcam_demo/ pi@<raspberry-pi-ip>:/home/pi/
```

Or clone project directory directly if hosted on GitHub.

### 4. Run the Object Detection Demo

```bash
cd tflite_rpi_webcam_demo
python3 detect.py
```

### 5. View Results

- A webcam window will open showing live video
- Detected objects will have bounding boxes and labels
- Press `q` to exit the window

---

## 📝 Sample `labelmap.txt`

This file contains the labels corresponding to model output classes:

```
person
bicycle
car
motorcycle
airplane
bus
train
truck
boat
traffic light
fire hydrant
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
```

---

## ✅ Notes

- If you want to use **Pi Camera**, modify the `cv2.VideoCapture()` line using `picamera2` or similar libraries.
- Ensure lighting conditions are good for better detection.
- USB webcams are generally more plug-and-play than CSI cameras.

---

## 🛠️ Troubleshooting

- **No camera feed?**
    - Try `cv2.VideoCapture(1)` or `0`
    - Check camera connection with `ls /dev/video*`

- **Model too slow?**
    - Use smaller model like `efficientdet_lite0`
    - Consider adding Coral USB Accelerator for real-time speed

---

## 📬 Credits

- TensorFlow Lite team
- COCO dataset class labels
- OpenCV for real-time video processing
