import paho.mqtt.client as mqtt
import ssl

PI_ID = "subscriber1"
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "power/raspiX/data"

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print("Connection received")
    print(f"[{PI_ID}] Connected with result code {rc}")
    client.subscribe(TOPIC)

# Callback when a message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[{PI_ID}] Received: {payload} W on topic {msg.topic}")

# Create MQTT client
client = mqtt.Client(client_id=PI_ID)

# Optional TLS setup (test broker uses public CA, so we can allow insecure)
#client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
#client.tls_insecure_set(True)

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect and loop
client.connect(BROKER, PORT)
client.loop_forever()
