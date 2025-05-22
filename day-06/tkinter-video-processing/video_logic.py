# video_logic.py
import cv2
import numpy as np

class VideoProcessor:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.use_grayscale = False
        self.filter_mode = None
        self.brightness = 1.0
        self.contrast = 0

    def set_grayscale(self, use_gray):
        self.use_grayscale = use_gray

    def set_filter(self, mode):
        self.filter_mode = mode

    def set_brightness(self, value):
        self.brightness = value

    def set_contrast(self, value):
        self.contrast = value

    def process_frame(self, frame):
        frame = cv2.convertScaleAbs(frame, alpha=self.brightness, beta=self.contrast)

        # Convert to grayscale if required
        if self.use_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Apply filter
        if self.filter_mode == "sobel":
            sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
            frame = cv2.convertScaleAbs(cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0))
        elif self.filter_mode == "gaussian":
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        elif self.filter_mode == "median":
            frame = cv2.medianBlur(frame, 5)

        # Detect and draw faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame
