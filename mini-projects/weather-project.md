# 🧪 Assessment: IoT Weather Display & Alert System

## 🧩 Objective
Build a Python-based client-server system where the **laptop** fetches real-time weather data from the **OpenWeather API** and sends it to the **Raspberry Pi 5** over a **Wi-Fi network using Python sockets**.

The Raspberry Pi will:
- Display key weather information (temperature, pressure, weather condition) on the **OLED display** of the Pioneer600 HAT.
- Automatically **turn on an LED (GPIO26)** if the temperature exceeds a predefined threshold.

---

## 🛠️ System Architecture

### Laptop (Client)
- Fetch weather data using **OpenWeatherMap API**
- Extract:
  - Temperature (°C)
  - Pressure (hPa)
  - Weather condition (e.g., Clear, Rain)
- Send data to Raspberry Pi via socket connection (JSON format recommended)

### Raspberry Pi (Server)
- Accept incoming socket connections
- Parse and display received weather data on the OLED (Pioneer600 HAT)
- Turn ON/OFF an LED on GPIO26 based on temperature threshold

---

## 📦 Requirements

### Laptop
- Python 3
- Libraries:
  - `requests`
  - `socket`

### Raspberry Pi 5 (Bookworm OS)
- Pioneer600 HAT
- Python 3
- Libraries:
  - `socket`
  - `json`
  - `gpiozero`
  - `time`
  - OLED display driver (`luma.oled` or Waveshare library)

---

## ✅ Tasks Breakdown

### Client Side (Laptop)
1. Get OpenWeatherMap API key: [https://openweathermap.org/](https://openweathermap.org/)
2. Write script to:
   - Fetch weather for a city
   - Extract temp, pressure, condition
   - Connect to Raspberry Pi's IP
   - Send data as JSON string

### Server Side (Raspberry Pi)
1. Setup socket server
2. Receive and parse data
3. Display on OLED:
   ```
   Temp: XX.X°C
   Press: XXXX hPa
   Cond: Clear
   ```
4. Turn on LED (GPIO26) if temperature > 30°C

---

## 🧪 Evaluation Criteria

| Criteria                                  | Marks |
|-------------------------------------------|-------|
| Weather data correctly fetched & parsed   | 10    |
| Reliable socket communication             | 15    |
| Correct display on OLED                   | 15    |
| LED logic works as intended               | 10    |
| Code quality and modularity               | 5     |
| Bonus: Configurable threshold, error handling | +5 |

---

## 📝 Deliverables

- Python script for **client (laptop)** and **server (Pi)**
- Short demo video or live demo
- README file explaining setup, usage, and test results
