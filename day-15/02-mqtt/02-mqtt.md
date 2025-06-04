📌 Title: Python MQTT Client Pair
Objective: Simulate a basic IoT device sending sensor-like data using MQTT in Python.

Instructions:

Create a script (mqtt_sensor.py) that:

Connects to the broker.

Publishes a message (e.g., a simulated temperature) every 5 seconds to topic sensor/temp.

Create another script (mqtt_monitor.py) that:

Subscribes to sensor/temp.

Prints each received message to the terminal.

(Optional Enhancement):

Send random temperature values using random.uniform().

Add timestamp to the payload.

---------------------------------------------------------------------------

# mqtt_sensor.py
import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client("Sensor1")
client.connect("localhost")

while True:
    temp = round(random.uniform(20.0, 30.0), 2)
    client.publish("sensor/temp", f"Temperature: {temp}°C")
    time.sleep(5)


# mqtt_monitor.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received ->", message.payload.decode())

client = mqtt.Client("Monitor1")
client.connect("localhost")

client.subscribe("sensor/temp")
client.on_message = on_message
client.loop_forever()
