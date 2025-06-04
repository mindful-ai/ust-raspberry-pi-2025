import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on topic {msg.topic}")

broker = "broker.hivemq.com"
topic = "iot/workshop/device1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "subscriber")
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)

client.loop_forever()
