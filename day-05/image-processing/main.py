# main.py
import tkinter as tk
from face_gui import FaceDetectionApp

def main():
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
