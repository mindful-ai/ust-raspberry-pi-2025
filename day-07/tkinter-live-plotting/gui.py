# gui.py

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class BitcoinPriceGUI:
    def __init__(self, root, data_callback):
        self.root = root
        self.data_callback = data_callback

        self.root.title("Live Bitcoin Price Tracker")
        self.fig, self.ax = plt.subplots(figsize=(6, 4))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Start", command=self.start).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Stop", command=self.stop).pack(side=tk.LEFT, padx=5)

        self.update_interval = 5000  # 5 seconds
        self.running = False

    def start(self):
        self.running = True
        self.update_plot()

    def stop(self):
        self.running = False

    def update_plot(self):
        if not self.running:
            return

        timestamps, prices = self.data_callback()
        self.ax.clear()

        self.ax.plot(timestamps, prices, marker='o', color='blue')
        self.ax.set_title("Bitcoin Price (USD)")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Price")
        self.ax.tick_params(axis='x', rotation=45)

        self.fig.tight_layout()
        self.canvas.draw()

        self.root.after(self.update_interval, self.update_plot)
