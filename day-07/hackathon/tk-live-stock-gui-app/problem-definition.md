# 📈 Assessment: Live Plotting of Indian Stock Prices using Tkinter

## Objective

Design and develop a Python application that provides a **Tkinter-based GUI** to **plot live stock prices** of Indian companies. The application should continuously fetch live price data and update the plot in real time using `matplotlib`.

---

## 🧠 Learning Outcomes

- Understanding of GUI development using `Tkinter`
- Real-time data plotting using `matplotlib.animation`
- API integration for fetching live data
- Modular programming (separation of GUI, logic, and integration)

---

## 🛠 Requirements

1. **GUI Requirements (Tkinter):**
   - A simple window showing:
     - A dropdown or entry box to select the **stock symbol** (e.g., TCS, INFY, RELIANCE)
     - A **Start** button to begin live plotting
     - A **Stop** button to halt data fetching
     - A **Matplotlib** embedded plot area showing price changes over time

2. **Live Data Source:**
   - Use the [NSE India API via `nsetools`](https://github.com/vsjha18/nsetools) or `yfinance` library for simplicity.
   - Example for fetching data:
     ```python
     import yfinance as yf
     stock = yf.Ticker("TCS.NS")  # NSE ticker
     price = stock.history(period="1d", interval="1m").tail(1)['Close'].values[0]
     ```
   - Symbols must end with `.NS` for Indian stocks (e.g., TCS.NS, RELIANCE.NS, INFY.NS)

3. **Plotting Requirements:**
   - Show a live line chart with:
     - X-axis: Timestamps
     - Y-axis: Stock price
   - The plot should update every **60 seconds** with new data.
   - Keep the last 20 data points visible for clarity.

4. **Code Structure:**
   - `logic.py`: Contains functions to fetch live stock data.
   - `gui.py`: Contains Tkinter and Matplotlib GUI logic.
   - `main.py`: Integrates the logic and GUI.

---

## ✅ Evaluation Criteria

- Correct implementation of API fetching and real-time plotting
- Functional and responsive GUI
- Clear code structure with separation of concerns
- Code readability and comments

---

## ⏱ Bonus (Optional)

- Allow user to select refresh interval (30s, 1min, 5min)
- Enable plotting of multiple stocks simultaneously
- Add a "Save Data" button to export current data to a CSV

---

## 🔧 Setup Instructions

Install necessary libraries:

```bash
pip install yfinance matplotlib tkinter
