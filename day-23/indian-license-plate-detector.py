import cv2
import easyocr
import tkinter as tk
from PIL import Image, ImageTk
import re

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Tkinter App
class LicensePlateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Indian License Plate Recognition")
        self.root.geometry("800x600")

        # Video display
        self.label = tk.Label(root)
        self.label.pack()

        # Result display
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 24), fg="blue")
        self.result_label.pack(pady=20)

        # Button to trigger recognition
        self.capture_button = tk.Button(root, text="Capture & Recognize", command=self.capture_and_recognize)
        self.capture_button.pack()

        # Start video stream
        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame.copy()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def format_plate(self, text):
        # Try matching the pattern KA01AB1234
        match = re.findall(r'([A-Z]{2}\s*\d{1,2}\s*[A-Z]{1,2}\s*\d{3,4})', text.replace('\n', '').upper())
        if match:
            return match[0].replace(" ", "")
        return "No valid plate found"

    def capture_and_recognize(self):
        gray = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2GRAY)
        results = reader.readtext(gray)

        for bbox, text, conf in results:
            formatted = self.format_plate(text)
            if "No valid" not in formatted:
                self.result_var.set(f"Detected: {formatted}")
                return

        self.result_var.set("License Plate Not Detected")

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LicensePlateApp(root)
    root.mainloop()
