
# Advanced Python Generator with `yield` and `send()` – Sensor Example

This example demonstrates an advanced use of Python generators using `yield` and `send()` to handle **real-time temperature sensor data**, commonly used in IoT scenarios like Raspberry Pi.

---

## 🎯 Use Case

You're receiving **temperature sensor data** (e.g., from a Raspberry Pi). You want a generator that:
- Receives temperature values using `.send()`
- Prints warnings for high temperatures
- Keeps running until explicitly stopped

---

## 🧪 Code: Real-Time Temperature Monitor

```python
def temperature_monitor(threshold=30):
    print(f"🌡️ Monitor started. Alert if temperature exceeds {threshold}°C")
    while True:
        temp = yield  # Wait for incoming temperature
        if temp is None:
            print("🛑 Monitor stopped.")
            break
        elif temp > threshold:
            print(f"🚨 Alert! High temperature detected: {temp}°C")
        else:
            print(f"✅ Temperature normal: {temp}°C")

# Create the generator
monitor = temperature_monitor()

# Start the coroutine
next(monitor)

# Simulate sensor readings
monitor.send(25)   # Normal
monitor.send(32)   # High
monitor.send(28)   # Normal
monitor.send(35)   # High

# Stop the monitor
try:
    monitor.send(None)  # Sending None to signal stop
except StopIteration:
    pass
```

---

## 🧾 Sample Output

```
🌡️ Monitor started. Alert if temperature exceeds 30°C
✅ Temperature normal: 25°C
🚨 Alert! High temperature detected: 32°C
✅ Temperature normal: 28°C
🚨 Alert! High temperature detected: 35°C
🛑 Monitor stopped.
```

---

## ✅ Why This Pattern is Powerful

- **Non-blocking**: Keeps running in a loop without blocking.
- **Two-way data flow**: External code sends real-time data.
- **Efficient**: Maintains internal state.
- **Control**: Pause/resume, and dynamically respond to input.

---

## 🔁 Extension Ideas

- Accept a dictionary like `{'sensor': 'temp', 'value': 34}` to support multiple sensor types.
- Log data to a file or visualize in real time.
- Wrap in `asyncio` or trigger from a hardware interrupt.
- Integrate with MQTT or sensor libraries like `Adafruit_BMP280`.

---

## 📚 Related Topics

- Python Generators
- Coroutines
- `yield` and `send()`
- Real-time data processing
- IoT programming with Raspberry Pi
