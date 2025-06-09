
# 🔁 HIL Testing of Pressure & Temperature Using Raspberry Pi (Pioneer600) and Laptop with TCP/IP

## 🧠 Objective

Perform **Hardware-in-the-Loop (HIL)** testing where:

- **Raspberry Pi** (with Pioneer600 HAT) reads **pressure and temperature**.
- A **pytest test suite** runs on the **laptop** and validates sensor data.
- **TCP/IP** is used for communication.
- Communication layer is cleanly separated into **server** and **client** modules.

---

## 🧱 Folder Structure

```
hil_tcp_project/
├── raspberry_pi/
│   ├── gpio_sensor.py         # Reads pressure & temperature from Pioneer600
│   └── server.py              # TCP server (runs on Pi)
├── laptop/
│   ├── test_hil.py            # pytest test suite (runs on Laptop)
│   └── client.py              # TCP client (connects to Pi)
```

---

## 📜 `gpio_sensor.py` (Raspberry Pi)

```python
# raspberry_pi/gpio_sensor.py
import random

# Simulated values - replace with actual sensor code if needed
def read_temperature():
    # Insert actual I2C/SPI sensor read logic here
    return round(random.uniform(25.0, 40.0), 2)

def read_pressure():
    # Insert actual sensor read logic
    return round(random.uniform(900.0, 1050.0), 2)
```

---

## 📜 `server.py` (Raspberry Pi)

```python
# raspberry_pi/server.py
import socket
import json
from gpio_sensor import read_temperature, read_pressure

HOST = '0.0.0.0'
PORT = 5005

def get_sensor_data():
    return {
        "temperature": read_temperature(),
        "pressure": read_pressure()
    }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Pi Server] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[Connection] From {addr}")
            data = conn.recv(1024)
            if data:
                try:
                    request = json.loads(data.decode())
                    if request.get("command") == "get_data":
                        response = get_sensor_data()
                    else:
                        response = {"error": "Unknown command"}
                except Exception as e:
                    response = {"error": str(e)}
                conn.sendall(json.dumps(response).encode())
```

---

## 📜 `client.py` (Laptop)

```python
# laptop/client.py
import socket
import json

PI_IP = "192.168.1.42"  # Replace with actual Raspberry Pi IP
PORT = 5005

def fetch_sensor_data():
    request = json.dumps({"command": "get_data"}).encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PI_IP, PORT))
        s.sendall(request)
        data = s.recv(1024)
        return json.loads(data.decode())
```

---

## 📜 `test_hil.py` (Laptop - pytest suite)

```python
# laptop/test_hil.py
import pytest
from client import fetch_sensor_data

def test_temperature_range():
    data = fetch_sensor_data()
    assert 20.0 <= data["temperature"] <= 50.0, f"Unexpected temperature: {data['temperature']}"

def test_pressure_range():
    data = fetch_sensor_data()
    assert 850.0 <= data["pressure"] <= 1100.0, f"Unexpected pressure: {data['pressure']}"
```

---

## 🧪 Instructions to Run

### ✅ On Raspberry Pi:
1. **Enable I2C/SPI** on Raspberry Pi.
2. **Install packages**:

```bash
sudo apt update
sudo apt install python3-gpiozero python3-pip
```

3. **Run the server**:

```bash
cd hil_tcp_project/raspberry_pi
python3 server.py
```

---

### ✅ On Laptop:
1. **Install pytest**:

```bash
pip install pytest
```

2. **Run the tests**:

```bash
cd hil_tcp_project/laptop
pytest test_hil.py
```

> Ensure Raspberry Pi and laptop are on the same network. Update IP in `client.py` accordingly.

---

## ✅ Summary

| File                      | Role                                |
|---------------------------|-------------------------------------|
| `gpio_sensor.py`          | Reads real/simulated hardware data  |
| `server.py`               | TCP server on Raspberry Pi          |
| `client.py`               | TCP client on laptop                |
| `test_hil.py`             | pytest-based HIL test suite         |

---

This setup makes it easy to **test real hardware remotely** using structured unit tests from a dev machine. 🌐🔧🧪
