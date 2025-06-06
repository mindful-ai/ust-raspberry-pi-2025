import paho.mqtt.client as mqtt
import time
import random
import json

broker = "test.mosquitto.org"
port = 1883
topic = "demo/temperature/purush"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temperature = round(random.uniform(20, 40), 2)
    payload = json.dumps({"temperature": temperature})
    client.publish(topic, payload)
    print("Published:", payload)
    time.sleep(5)