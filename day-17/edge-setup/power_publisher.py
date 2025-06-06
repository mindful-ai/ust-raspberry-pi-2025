import paho.mqtt.client as mqtt
import ssl
import time
import random
import socket

PI_ID = 'raspi1'  # Use hostname as unique ID
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_PUB = f"power/raspi1/data"
TOPIC_CMD = f"power/raspi1/command"

client = mqtt.Client(client_id='Publisher')

# TLS setup
# client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
# client.tls_insecure_set(False)

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