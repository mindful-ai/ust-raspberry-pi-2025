import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()} on topic {message.topic}")

broker_address = "localhost"

client = mqtt.Client("Subscriber1")
client.connect(broker_address)

client.subscribe("home/test")
client.on_message = on_message

print("Subscribed. Waiting for messages...")
client.loop_forever()
