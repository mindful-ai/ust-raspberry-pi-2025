# main.py
import tkinter as tk
from video_gui import VideoFaceApp

def main():
    root = tk.Tk()
    app = VideoFaceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
