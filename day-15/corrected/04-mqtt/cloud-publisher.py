import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic = "iot/workshop/device1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "raspi_publisher")
client.connect(broker, port)

while True:
    message = "Hello from Raspberry Pi"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(5)
