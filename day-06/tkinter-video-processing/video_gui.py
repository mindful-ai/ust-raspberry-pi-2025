# video_gui.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from video_logic import VideoProcessor

class VideoFaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Face Detection with Filters")

        self.processor = VideoProcessor()
        self.cap = cv2.VideoCapture(0)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Grayscale", command=lambda: self.processor.set_grayscale(True)).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Color", command=lambda: self.processor.set_grayscale(False)).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Sobel", command=lambda: self.processor.set_filter("sobel")).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Gaussian", command=lambda: self.processor.set_filter("gaussian")).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Median", command=lambda: self.processor.set_filter("median")).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="None", command=lambda: self.processor.set_filter(None)).grid(row=0, column=5, padx=5)

        # Sliders
        slider_frame = tk.Frame(root)
        slider_frame.pack(pady=10)

        tk.Label(slider_frame, text="Brightness").grid(row=0, column=0)
        self.brightness_slider = tk.Scale(slider_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
                                          command=lambda val: self.processor.set_brightness(float(val)))
        self.brightness_slider.set(1.0)
        self.brightness_slider.grid(row=0, column=1)

        tk.Label(slider_frame, text="Contrast").grid(row=0, column=2)
        self.contrast_slider = tk.Scale(slider_frame, from_=-100, to=100, orient=tk.HORIZONTAL,
                                        command=lambda val: self.processor.set_contrast(int(val)))
        self.contrast_slider.set(0)
        self.contrast_slider.grid(row=0, column=3)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            processed = self.processor.process_frame(frame)
            img = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.imgtk = imgtk
            self.canvas.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def __del__(self):
        self.cap.release()
