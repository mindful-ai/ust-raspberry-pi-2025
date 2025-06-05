import paho.mqtt.client as mqtt
import ssl

BROKER = "test.mosquitto.org"
PORT = 8883
TOPIC = "iot/simple/secure"

def on_connect(client, userdata, flags, rc):
    print("[Subscriber] Connected.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"[Subscriber] Received: {msg.payload.decode()}")

client = mqtt.Client()

# TLS settings
client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(False)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
