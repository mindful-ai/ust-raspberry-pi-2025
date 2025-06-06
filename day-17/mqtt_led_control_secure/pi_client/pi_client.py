# pi_client/pi_client.py

from gpiozero import LED
import paho.mqtt.client as mqtt
import time
import ssl
from common import config

PI_ID = "pi1"  # Change this for each Pi
led = LED(24)  # GPIO24 (Pioneer600 D4)

def on_connect(client, userdata, flags, rc):
    print(f"[{PI_ID}] Connected with result code {rc}")
    client.subscribe(f"pi/{PI_ID}/led/control")

def on_message(client, userdata, msg):
    payload = msg.payload.decode().strip()
    print(f"[{PI_ID}] Received: {payload}")
    if payload == "ON":
        led.on()
        status = "ON"
    elif payload == "OFF":
        led.off()
        status = "OFF"
    else:
        status = "UNKNOWN"
    client.publish(f"pi/{PI_ID}/led/status", status)

client = mqtt.Client()
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set(ca_certs=config.CA_CERT, cert_reqs=ssl.CERT_REQUIRED)
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, config.PORT, 60)
client.loop_forever()
