from ui.hmi_view import BoilerHMI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = BoilerHMI(root)
    root.mainloop()
