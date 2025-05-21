# face_logic.py
import cv2

class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def detect_faces(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            return False, "Image could not be read.", None

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(faces) > 0:
            return True, f"{len(faces)} face(s) detected.", image
        else:
            return False, "No faces detected.", image
