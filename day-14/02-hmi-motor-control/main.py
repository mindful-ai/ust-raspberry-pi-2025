from ui.hmi_view import MotorHMI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MotorHMI(root)
    root.mainloop()
