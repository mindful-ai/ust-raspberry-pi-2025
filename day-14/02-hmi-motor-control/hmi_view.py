import tkinter as tk
from tkinter import ttk
from controller.motor_controller import MotorController
from controller.logger import log

class MotorHMI:
    def __init__(self, root):
        self.root = root
        self.root.title("Industrial Motor Controller HMI")
        self.root.geometry("800x480")
        self.root.configure(bg="black")

        self.controller = MotorController()

        self.title_font = ("Helvetica", 24, "bold")
        self.label_font = ("Helvetica", 20)
        self.button_font = ("Helvetica", 20)
        self.status_font = ("Helvetica", 18)

        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=20)

        # Speed control
        speed_frame = tk.LabelFrame(frame, text="Speed (RPM)", font=self.title_font, fg="white", bg="black", padx=20, pady=20)
        speed_frame.grid(row=0, column=0, padx=30, pady=20)

        self.speed_slider = tk.Scale(speed_frame, from_=0, to=3000, orient=tk.HORIZONTAL, length=600,
                                     command=self.on_speed_change, font=self.label_font, tickinterval=500, resolution=100,
                                     bg="gray20", fg="white", troughcolor="gray40", highlightthickness=0)
        self.speed_slider.set(1500)
        self.speed_slider.pack()

        # Direction control
        dir_frame = tk.LabelFrame(frame, text="Direction", font=self.title_font, fg="white", bg="black", padx=20, pady=20)
        dir_frame.grid(row=1, column=0, padx=30, pady=20)

        self.fwd_button = tk.Button(dir_frame, text="Forward", command=lambda: self.set_direction("Forward"),
                                    font=self.button_font, width=15, height=2, bg="green", fg="white")
        self.fwd_button.pack(pady=10)

        self.rev_button = tk.Button(dir_frame, text="Reverse", command=lambda: self.set_direction("Reverse"),
                                    font=self.button_font, width=15, height=2, bg="red", fg="white")
        self.rev_button.pack(pady=10)

        # Start/Stop controls
        control_frame = tk.LabelFrame(frame, text="Controls", font=self.title_font, fg="white", bg="black", padx=20, pady=20)
        control_frame.grid(row=2, column=0, padx=30, pady=20)

        self.start_button = tk.Button(control_frame, text="Start", command=self.start_motor,
                                      font=self.button_font, width=15, height=2, bg="blue", fg="white")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_motor,
                                     font=self.button_font, width=15, height=2, bg="gray", fg="white")
        self.stop_button.pack(pady=10)

        # Status
        self.status_label = tk.Label(self.root, text="", font=self.status_font, fg="yellow", bg="black")
        self.status_label.pack(pady=10)

    def on_speed_change(self, value):
        rpm = int(float(value))
        self.controller.set_speed(rpm)
        log(f"Speed set to {rpm} RPM")

    def set_direction(self, direction):
        self.controller.set_direction(direction)
        log(f"Direction set to {direction}")

    def start_motor(self):
        self.controller.start()
        log("Motor started")
        self.update_status()

    def stop_motor(self):
        self.controller.stop()
        log("Motor stopped")
        self.update_status()

    def update_status(self):
        status = f"Motor: {'ON' if self.controller.running else 'OFF'} | "                  f"Speed: {self.controller.speed} RPM | "                  f"Direction: {self.controller.direction}"
        self.status_label.config(text=status)
        self.root.after(1000, self.update_status)