import paho.mqtt.client as mqtt
import time

broker_address = "localhost"  # Or IP of your Raspberry Pi

client = mqtt.Client("Publisher1")
client.connect(broker_address)

try:
    while True:
        client.publish("home/test", "Hello from Publisher")
        print("Message Published")
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting...")
