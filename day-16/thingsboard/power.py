import paho.mqtt.client as mqtt
import json
import random
import time


# mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "mewmswxmzzo8ulyz3yts" -m "{temperature:25}"

BROKER = "mqtt.thingsboard.cloud"  # Replace with your server if self-hosted
PORT = 1883
ACCESS_TOKEN = "mewmswxmzzo8ulyz3yts"  # Replace with your device token

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