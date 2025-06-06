import paho.mqtt.client as mqtt
import time
import random
import json

BROKER = "test.mosquitto.org"
TOPIC = "iot/sensors"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

try:
    while True:
        data = {
            "temperature": round(random.uniform(25, 35), 2),
            "pressure": round(random.uniform(1000, 1020), 2)
        }
        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)
        time.sleep(5)
except KeyboardInterrupt:
    client.disconnect()
