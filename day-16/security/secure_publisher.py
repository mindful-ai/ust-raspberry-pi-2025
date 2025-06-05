import paho.mqtt.client as mqtt
import ssl
import time

BROKER = "test.mosquitto.org"
PORT = 8883
TOPIC = "iot/simple/secure"

client = mqtt.Client()

# TLS settings
client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(False)  # Do NOT skip cert validation

client.connect(BROKER, PORT)

# Publish a simple message
msg = "Hello from secure publisher!"
client.publish(TOPIC, msg)
print(f"[Publisher] Sent: {msg}")

client.disconnect()
