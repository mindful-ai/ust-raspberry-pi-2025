# face_gui.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from face_logic import FaceDetector

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection App")

        self.detector = FaceDetector()

        self.label = tk.Label(root, text="Upload an image to detect faces", font=("Arial", 14))
        self.label.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if file_path:
            face_found, message, img_with_faces = self.detector.detect_faces(file_path)

            if img_with_faces is not None:
                # Convert OpenCV image (BGR) to PIL image (RGB) for Tkinter
                img_rgb = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_rgb)
                img_pil.thumbnail((400, 400))  # Resize for display
                photo = ImageTk.PhotoImage(img_pil)

                self.image_label.config(image=photo)
                self.image_label.image = photo

            self.result_label.config(text=message, fg="green" if face_found else "red")
