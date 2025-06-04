import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
	print(f"Message received: {message.payload.decode()} on topic {message.topic}")

broker_addr = "localhost"

#client = mqtt.Client(client_id="Subscriber1", callback_api_version=4)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Subscriber1")
client.connect(broker_addr)

client.subscribe("home/test")
client.on_message = on_message

print("Subscribed. Waiting for messages...")
client.loop_forever()
