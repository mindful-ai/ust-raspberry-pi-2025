import paho.mqtt.client as mqtt
import requests
import json

broker = "test.mosquitto.org"
topic = "sensors/room1/temp"
endpoint = "https://httpbin.org/post"

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[MQTT] Received: {payload}")
    
    data = {
        "device_id": "room1_sensor",
        "type": "temperature",
        "value": float(payload)
    }

    response = requests.post(endpoint, json=data)
    print(f"[HTTP] Sent to cloud. Status: {response.status_code}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("[Agent] Starting MQTT agent...")
client.connect(broker, 1883, 60)
client.loop_forever()
