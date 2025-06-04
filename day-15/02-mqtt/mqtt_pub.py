import paho.mqtt.client as mqtt
import time

broker_address = "localhost"

#client = mqtt.Client("Publisher1")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Publisher1")


client.connect(broker_address)


try:
	while True:
		client.publish("home/test", "Hello from Publisher")
		print("Message Published")
		time.sleep(3)
except KeyboardInterrupt:
	print("Exiting...")
