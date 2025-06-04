import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

# client = mqtt.Client("BMP280_Subscriber")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "BMP280_Subscriber")
client.connect("localhost")
client.subscribe("sensor/bmp280")
client.on_message = on_message
client.loop_forever()
