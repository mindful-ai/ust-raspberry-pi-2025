# 🧪 Assessment: IoT Agent Implementation with MQTT and HTTP

## 🎯 Problem Statement

You are tasked with developing a **Python-based IoT Agent** for a temperature-sensing device.

### Requirements:

1. **Device Simulation**:
   - Simulate a temperature sensor that publishes a random temperature value (between 15°C and 40°C) to an MQTT broker every 10 seconds.
   - Use the MQTT topic: `sensors/room1/temp`.

2. **IoT Agent**:
   - Create a Python script that subscribes to the above MQTT topic.
   - On receiving a message:
     - Parse the temperature value.
     - Convert it to a JSON format:
       ```json
       {
         "device_id": "room1_sensor",
         "type": "temperature",
         "value": <temperature_value>
       }
       ```
     - Send this JSON payload via an HTTP POST request to the endpoint: `https://httpbin.org/post`.

3. **Logging**:
   - The agent should print:
     - The received MQTT message.
     - The HTTP status code after sending the POST request.

---

## 📌 Submission Checklist

- [ ] `mqtt_device_simulator.py`: Simulates temperature readings and publishes via MQTT.
- [ ] `iot_agent.py`: Subscribes to MQTT, processes the message, and sends it over HTTP.
- [ ] Console logs must show both MQTT reception and HTTP POST success.

---

## ✅ Evaluation Criteria

- MQTT device simulation correctness
- Data parsing and formatting
- Correct HTTP POST request and status handling
- Clean code and readable logs

---

## 🧠 Answer Key / Solution Summary

### ✅ mqtt_device_simulator.py (Publisher)

```python
import paho.mqtt.publish as publish
import time
import random

broker = "test.mosquitto.org"
topic = "sensors/room1/temp"

while True:
    temp = round(random.uniform(15.0, 40.0), 2)
    publish.single(topic, str(temp), hostname=broker)
    print(f"[Device] Sent temperature: {temp}°C")
    time.sleep(10)
