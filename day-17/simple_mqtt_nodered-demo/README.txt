# 🌡️ Simple MQTT Temperature Demo with Node-RED and Python

## 🧩 Overview
- Publishes temperature values to a **public MQTT broker** (`test.mosquitto.org`).
- Node-RED (running in Docker) connects to the same broker.
- Live temperature updates are shown on a dashboard.

## ✅ Setup Instructions

### 1. Run the Python Publisher (on Windows)
Install MQTT library:
```
pip install paho-mqtt
```

Run the script:
```
python simple_publisher.py
```

### 2. Run Node-RED Docker Container
```
docker run -it -p 1880:1880 --name nodered-demo nodered/node-red
```

Open Node-RED: [http://localhost:1880](http://localhost:1880)

### 3. Create Node-RED Flow

#### Nodes Required:
- `mqtt in` (topic: `demo/temperature/purush`, broker: `test.mosquitto.org`, port `1883`)
- `json` node
- `ui_gauge` node

#### Flow:
```
[mqtt in] → [json] → [ui_gauge]
```

Dashboard URL: [http://localhost:1880/ui](http://localhost:1880/ui)

You’ll see a live temperature gauge updating every 5 seconds.