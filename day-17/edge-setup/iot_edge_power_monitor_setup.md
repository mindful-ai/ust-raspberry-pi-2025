
# ⚡ IoT Edge Power Monitoring Demo (with MQTT and Dashboard Control)

This guide sets up 5 Raspberry Pi devices to simulate power data and securely publish it using MQTT. Windows PCs will subscribe and display a live dashboard and allow remote power reset commands.

---

## 📦 Components

- **5 Raspberry Pis** (Edge devices)
- **MQTT Broker** (Mosquitto test server or local secured broker)
- **Windows PC Clients** with real-time dashboard

---

## 🛠️ 1. Raspberry Pi Setup (Publisher)

### 📁 File: `power_publisher.py`

```python
import paho.mqtt.client as mqtt
import ssl
import time
import random
import socket

PI_ID = socket.gethostname()  # Use hostname as unique ID
BROKER = "test.mosquitto.org"
PORT = 8883
TOPIC_PUB = f"power/{PI_ID}/data"
TOPIC_CMD = f"power/{PI_ID}/command"

client = mqtt.Client()

# TLS setup
client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(False)

def on_connect(client, userdata, flags, rc):
    print(f"[{PI_ID}] Connected with result code {rc}")
    client.subscribe(TOPIC_CMD)

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    print(f"[{PI_ID}] Received command: {command}")
    if command == "RESET":
        print(f"[{PI_ID}] Resetting power stats...")

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        power = round(random.uniform(150.0, 300.0), 2)
        client.publish(TOPIC_PUB, str(power))
        print(f"[{PI_ID}] Published power: {power} W")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

Place `mosquitto.org.crt` in the same directory.

---

## 💻 2. Windows Client Setup (Dashboard + Command Sender)

### 📁 File: `dashboard_client.py`

```python
import paho.mqtt.client as mqtt
import ssl
import tkinter as tk
from collections import defaultdict

BROKER = "test.mosquitto.org"
PORT = 8883
PI_IDS = [f"raspi{i}" for i in range(1, 6)]  # Replace with actual Pi hostnames

power_data = defaultdict(lambda: "Waiting...")
clients = {}

def create_gui():
    window = tk.Tk()
    window.title("IoT Power Monitor Dashboard")

    labels = {}
    for pi_id in PI_IDS:
        frame = tk.Frame(window)
        frame.pack(pady=5)
        tk.Label(frame, text=pi_id, width=20).pack(side=tk.LEFT)
        label = tk.Label(frame, text="-- W", width=10)
        label.pack(side=tk.LEFT)
        labels[pi_id] = label
        btn = tk.Button(frame, text="Reset", command=lambda i=pi_id: send_reset(i))
        btn.pack(side=tk.LEFT)

    def update_labels():
        for pi_id in PI_IDS:
            labels[pi_id].config(text=f"{power_data[pi_id]} W")
        window.after(1000, update_labels)

    update_labels()
    return window

def send_reset(pi_id):
    clients[pi_id].publish(f"power/{pi_id}/command", "RESET")
    print(f"[Dashboard] Sent RESET to {pi_id}")

def make_client(pi_id):
    client = mqtt.Client()
    client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(False)

    def on_connect(client, userdata, flags, rc):
        topic = f"power/{pi_id}/data"
        client.subscribe(topic)
        print(f"[Dashboard] Subscribed to {topic}")

    def on_message(client, userdata, msg):
        power_data[pi_id] = msg.payload.decode()

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_start()
    return client

for pi_id in PI_IDS:
    clients[pi_id] = make_client(pi_id)

app = create_gui()
app.mainloop()
```

---

## 📁 3. Setup Steps

### 🔧 On Each Raspberry Pi

1. Save `power_publisher.py`
2. Save `mosquitto.org.crt` from: https://test.mosquitto.org/ssl/mosquitto.org.crt
3. Run the script:
   ```bash
   python3 power_publisher.py
   ```

### 🖥️ On Windows PC

1. Install `paho-mqtt`:
   ```bash
   pip install paho-mqtt
   ```

2. Download and save `mosquitto.org.crt` in the script directory.
3. Run the dashboard:
   ```bash
   python dashboard_client.py
   ```

---

## ✅ Output

- Each Pi publishes simulated power values securely every 5 seconds.
- Dashboard updates in real time.
- Clicking "Reset" sends an MQTT command to that Pi.

---

## 🛡️ Security Highlights

- TLS encryption with public CA cert
- MQTT broker communication on port 8883
- Command control channel secured over MQTT

---

## 🧠 Tips

- Replace `raspi1`, `raspi2`, etc., with real hostnames from `socket.gethostname()` on each Pi.
- You can scale up easily by adding more devices.

---

Happy IoT experimenting! 🌍📡⚡
