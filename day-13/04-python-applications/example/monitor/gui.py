import tkinter as tk
from tkinter import messagebox
from threading import Event
from monitor.sensor_simulator import SensorSimulator
from monitor.logger import log_data_to_csv

class EnvironmentMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulated Raspberry Pi Environment Monitor")
        self.stop_event = Event()
        self.simulator = None
        self.temperature = 0.0
        self.humidity = 0.0

        # Thresholds
        self.temp_threshold = tk.DoubleVar(value=35.0)
        self.humidity_threshold = tk.DoubleVar(value=70.0)

        self.setup_ui()

    def setup_ui(self):
        # Display area
        self.temp_label = tk.Label(self.root, text="Temperature: -- °C", font=("Arial", 14))
        self.humidity_label = tk.Label(self.root, text="Humidity: -- %", font=("Arial", 14))
        self.alert_label = tk.Label(self.root, text="", fg="red", font=("Arial", 12))

        self.temp_label.pack(pady=5)
        self.humidity_label.pack(pady=5)
        self.alert_label.pack(pady=5)

        # Threshold inputs
        tk.Label(self.root, text="Temp Threshold (°C):").pack()
        tk.Entry(self.root, textvariable=self.temp_threshold).pack()

        tk.Label(self.root, text="Humidity Threshold (%):").pack()
        tk.Entry(self.root, textvariable=self.humidity_threshold).pack()

        # Buttons
        self.start_button = tk.Button(self.root, text="Start Monitoring", command=self.start_monitoring)
        self.stop_button = tk.Button(self.root, text="Stop Monitoring", command=self.stop_monitoring)
        self.log_button = tk.Button(self.root, text="Log Data", command=self.log_data)

        self.start_button.pack(pady=5)
        self.stop_button.pack(pady=5)
        self.log_button.pack(pady=5)

    def update_display(self, temp, humid):
        self.temperature = temp
        self.humidity = humid
        self.temp_label.config(text=f"Temperature: {temp} °C")
        self.humidity_label.config(text=f"Humidity: {humid} %")

        if temp > self.temp_threshold.get() or humid > self.humidity_threshold.get():
            self.alert_label.config(text="⚠️ Threshold Exceeded!")
        else:
            self.alert_label.config(text="")

    def start_monitoring(self):
        if self.simulator and self.simulator.is_alive():
            messagebox.showinfo("Info", "Already monitoring.")
            return

        self.stop_event.clear()
        self.simulator = SensorSimulator(self.update_display, self.stop_event)
        self.simulator.start()

    def stop_monitoring(self):
        if self.simulator:
            self.stop_event.set()
            self.simulator.join()
            self.simulator = None
            self.alert_label.config(text="Monitoring stopped.")

    def log_data(self):
        log_data_to_csv("log.csv", self.temperature, self.humidity)
        messagebox.showinfo("Logged", "Data saved to log.csv")

def launch_gui():
    root = tk.Tk()
    app = EnvironmentMonitorApp(root)
    root.mainloop()
