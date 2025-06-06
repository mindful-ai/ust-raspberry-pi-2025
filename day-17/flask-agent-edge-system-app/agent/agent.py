import paho.mqtt.client as mqtt
import json
import requests

BROKER = "test.mosquitto.org"
TOPIC = "iot/sensors"
SERVER_URL = "http://localhost:5000/data"

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("Received from MQTT:", payload)
        res = requests.post(SERVER_URL, json=payload)
        print("Forwarded to Flask:", res.status_code)
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("Agent is running...")
client.loop_forever()
