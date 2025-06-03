import tkinter as tk
from controller.boiler_controller import BoilerController
from controller.logger import log, log_csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BoilerHMI:
    def __init__(self, root):
        self.root = root
        self.root.title("Boiler Controller HMI")
        self.root.geometry("1024x600")
        self.root.configure(bg="black")

        self.controller = BoilerController()

        self.title_font = ("Helvetica", 24, "bold")
        self.label_font = ("Helvetica", 20)
        self.button_font = ("Helvetica", 20)
        self.status_font = ("Helvetica", 18)

        self.pressure_history = []
        self.temp_history = []
        self.level_history = []

        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        top_frame = tk.Frame(self.root, bg="black")
        top_frame.pack(side=tk.TOP, pady=10)

        control_frame = tk.LabelFrame(top_frame, text="Controls", font=self.title_font, fg="white", bg="black", padx=20, pady=20)
        control_frame.grid(row=0, column=0, padx=20)

        self.start_button = tk.Button(control_frame, text="Start Boiler", command=self.start_boiler,
                                      font=self.button_font, width=15, height=2, bg="green", fg="white")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(control_frame, text="Stop Boiler", command=self.stop_boiler,
                                     font=self.button_font, width=15, height=2, bg="red", fg="white")
        self.stop_button.pack(pady=10)

        fuel_frame = tk.LabelFrame(top_frame, text="Fuel Rate", font=self.title_font, fg="white", bg="black", padx=20, pady=20)
        fuel_frame.grid(row=0, column=1, padx=20)

        self.fuel_slider = tk.Scale(fuel_frame, from_=0, to=10, orient=tk.HORIZONTAL, length=500,
                                    command=self.set_fuel_rate, font=self.label_font, resolution=0.5,
                                    bg="gray20", fg="white", troughcolor="gray40", highlightthickness=0)
        self.fuel_slider.set(5.0)
        self.fuel_slider.pack()

        self.status_label = tk.Label(self.root, text="", font=self.status_
