# logic.py
import cv2
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image

def convert_cv_qt(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(qt_image)
