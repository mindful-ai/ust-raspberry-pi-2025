
# ThingsBoard IoT Demo: Power Monitoring with Raspberry Pi and MQTT

## 🎯 Objective
Simulate power consumption on Raspberry Pi, publish to ThingsBoard via MQTT, and control the device (e.g., reset) using ThingsBoard RPC buttons.

---

## 🧱 Step 1: Set Up ThingsBoard

### Option A: Use ThingsBoard Cloud
- Go to [ThingsBoard Cloud](https://thingsboard.cloud)
- Sign up or log in
- Skip to Step 2

### Option B: Install Locally with Docker
```bash
docker run -p 8080:8080 --name thingsboard -d thingsboard/tb-postgres
```
- Access the dashboard at: http://localhost:8080
- Default credentials: `tenant@thingsboard.org` / `tenant`

---

## 🛠️ Step 2: Create Device in ThingsBoard

1. Login as **Tenant**
2. Go to **Devices → + Add Device**
3. Name: `PowerSensor01`
4. Save and open the device
5. Go to **Credentials tab** 
6. Copy the **Access Token** mewmswxmzzo8ulyz3yts

---

## 🐍 Step 3: Python MQTT Publisher (Raspberry Pi)

### Requirements:
```bash
pip install paho-mqtt
```

### Python Script (`power_publisher.py`)
```python
import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "demo.thingsboard.io"  # Replace with your server if self-hosted
PORT = 1883
ACCESS_TOKEN = "YOUR_DEVICE_ACCESS_TOKEN"  # Replace with your device token

TOPIC_TELEMETRY = "v1/devices/me/telemetry"
TOPIC_RPC = "v1/devices/me/rpc/request/+"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC_RPC)

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    try:
        payload = json.loads(msg.payload.decode())
        method = payload.get('method')
        if method == "resetPower":
            print("Reset command received!")
            # Custom logic to reset power
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

power_value = 100

try:
    while True:
        power_value += random.uniform(-5, 5)
        power_value = max(power_value, 0)

        telemetry = {"power": round(power_value, 2)}
        client.publish(TOPIC_TELEMETRY, json.dumps(telemetry))

        print(f"Published telemetry: {telemetry}")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

---

## 📊 Step 4: ThingsBoard Dashboard

1. Go to **Dashboards → + Add New Dashboard**
2. Add a **Timeseries Chart** widget:
   - Configure it to read the `power` telemetry.
3. Add a **RPC Button** widget:
   - Method name: `resetPower`
4. Save your dashboard

---

## ✅ Result

- Raspberry Pi sends live power data.
- ThingsBoard visualizes it.
- User can reset power with RPC button.

---

## 📝 Notes

- MQTT data is sent over TCP (unencrypted by default).
- You can enable TLS/SSL in ThingsBoard MQTT settings for production.
- ThingsBoard supports asset/device groups, alarms, rules, and more.

---

## 📦 Files Provided
- `power_publisher.py`: Python script to simulate and publish data
- (Optional) Dashboard export JSON available upon request
