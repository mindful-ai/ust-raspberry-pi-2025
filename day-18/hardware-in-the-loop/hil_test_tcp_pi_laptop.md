
# 🌐 Hardware-in-the-Loop (HIL) Testing Over TCP/IP with Raspberry Pi and Pioneer600 HAT

## 🧠 What is Hardware-in-the-Loop (HIL) Testing?

**Hardware-in-the-Loop (HIL)** testing connects real hardware to software running in a test environment. In this case, we run **pytest tests on a laptop**, while the **Raspberry Pi controls real hardware (e.g., LED)** via a **TCP/IP network**.

This allows:

- Safe and isolated test execution.
- Headless operation of Raspberry Pi.
- Scalable and distributed embedded system testing.

---

## 🎯 Goal

- Simulate a temperature reading on the **laptop**.
- Send it to the **Raspberry Pi** using TCP/IP.
- Raspberry Pi receives the temperature and activates an LED (via Pioneer600 HAT).
- Laptop receives back the LED state for validation.

---

## ⚙️ Architecture

```
Laptop (pytest client) ─────TCP─────▶ Raspberry Pi (LED controller)
                               ▲
                               └────────LED State Response
```

---

## 🧱 Folder Structure

```
hil_test_tcp/
├── pi_server/
│   └── gpio_server.py       # Runs on Raspberry Pi
├── laptop_tests/
│   └── test_remote_led.py   # Runs on laptop
```

---

## 📜 Raspberry Pi: `gpio_server.py`

```python
# pi_server/gpio_server.py

import socket
import json
from gpiozero import LED

HOST = "0.0.0.0"
PORT = 5001

led = LED(17)
TEMPERATURE_THRESHOLD = 30.0

def handle_request(data):
    temperature = data.get("temperature")
    if temperature is not None:
        led_state = temperature > TEMPERATURE_THRESHOLD
        led.value = led_state
        return {"led_state": led.is_lit}
    return {"error": "Invalid data"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on port", PORT)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            try:
                request = json.loads(data.decode())
                response = handle_request(request)
            except Exception as e:
                response = {"error": str(e)}
            conn.sendall(json.dumps(response).encode())
```

> 📝 Run this file on your Raspberry Pi.

---

## 📜 Laptop: `test_remote_led.py`

```python
# laptop_tests/test_remote_led.py

import pytest
import socket
import json

PI_IP = "192.168.1.42"  # Replace with Raspberry Pi IP
PORT = 5001

def send_temperature(temp):
    request = json.dumps({"temperature": temp}).encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PI_IP, PORT))
        s.sendall(request)
        response = s.recv(1024)
        return json.loads(response.decode())

def test_led_on_high_temp():
    response = send_temperature(35.0)
    assert response["led_state"] == True

def test_led_off_low_temp():
    response = send_temperature(25.0)
    assert response["led_state"] == False
```

> 📝 Run this test file on your **laptop** using `pytest`.

---

## 🧪 Steps to Run

1. **On Raspberry Pi:**

```bash
sudo apt install python3-gpiozero
python3 pi_server/gpio_server.py
```

2. **On Laptop:**

```bash
pip install pytest
pytest laptop_tests/test_remote_led.py
```

---

## 🔒 Notes

- Ensure the laptop and Pi are on the same network.
- Allow port 5001 through firewalls if necessary.
- You can enhance security with SSL, tokens, or ssh tunnels for production.

---

## ✅ Summary

| Component           | Role                            |
|---------------------|----------------------------------|
| Raspberry Pi        | Hardware server, controls LED   |
| Laptop              | Test client, simulates sensor   |
| `gpiozero.LED`      | GPIO abstraction on Pi          |
| `pytest`            | Test framework on laptop        |
| `socket` + JSON     | TCP/IP communication layer      |

---

Test over networks with real hardware — the right way! 🌐🔧
