### logic.py

import yfinance as yf
from datetime import datetime

def fetch_latest_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d", interval="1m")
        if not hist.empty:
            latest_time = hist.index[-1]
            latest_price = hist['Close'].iloc[-1]
            return latest_time, latest_price
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None


### gui.py

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import logic  # assumes logic.py is in the same directory

class StockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Stock Price Plotter")

        # Control Variables
        self.symbol_var = tk.StringVar(value="TCS.NS")
        self.running = False

        # GUI Setup
        self.setup_widgets()
        self.setup_plot()

        self.x_data = []
        self.y_data = []

    def setup_widgets(self):
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        ttk.Label(top_frame, text="Stock Symbol:").pack(side=tk.LEFT)
        self.symbol_entry = ttk.Entry(top_frame, textvariable=self.symbol_var, width=10)
        self.symbol_entry.pack(side=tk.LEFT, padx=5)

        self.start_button = ttk.Button(top_frame, text="Start", command=self.start_plotting)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(top_frame, text="Stop", command=self.stop_plotting)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def setup_plot(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-o')
        self.ax.set_title("Live Stock Price")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Price")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_plot(self, i):
        if self.running:
            time, price = logic.fetch_latest_price(self.symbol_var.get())
            if time and price:
                self.x_data.append(time)
                self.y_data.append(price)

                # Keep only last 20 points
                self.x_data = self.x_data[-20:]
                self.y_data = self.y_data[-20:]

                self.ax.clear()
                self.ax.plot(self.x_data, self.y_data, marker='o', linestyle='-')
                self.ax.set_title(f"Live Stock Price: {self.symbol_var.get()}")
                self.ax.set_xlabel("Time")
                self.ax.set_ylabel("Price")
                self.ax.tick_params(axis='x', rotation=45)
                self.ax.grid(True)
                self.fig.tight_layout()
                self.canvas.draw()

    def start_plotting(self):
        self.running = True

    def stop_plotting(self):
        self.running = False


### main.py

import tkinter as tk
from gui import StockGUI
import matplotlib.animation as animation

if __name__ == '__main__':
    root = tk.Tk()
    app = StockGUI(root)
    ani = animation.FuncAnimation(app.fig, app.update_plot, interval=60000)  # every 60 seconds
    root.mainloop()
