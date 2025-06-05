import paho.mqtt.client as mqtt
import requests
import json

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/device/temperature"

HTTP_ENDPOINT = "https://httpbin.org/post"  # Simulate cloud with this service

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[MQTT] Received: {payload}")
    
    # Parse and forward to HTTP endpoint
    try:
        data = {
            "device_id": "sensor_001",
            "type": "temperature",
            "value": float(payload)
        }
        response = requests.post(HTTP_ENDPOINT, json=data)
        print(f"[HTTP] Forwarded to cloud, status={response.status_code}")
    except Exception as e:
        print(f"[ERROR] {e}")

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("[INFO] Starting IoT Agent...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
