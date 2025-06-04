💻 Hands-On Exercise: MQTT with HiveMQ Cloud
✅ Step 1: Modify Publisher to Use HiveMQ
Edit your mqtt_sensor_publisher.py from Session 3:


client = mqtt.Client("cloud_publisher")
client.connect("broker.hivemq.com", 1883, 60)
Use topic like:

topic = "iot/pi/sensor01"
client.publish(topic, payload)
✅ Step 2: Modify Subscriber to Use HiveMQ
mqtt_sensor_subscriber.py


client = mqtt.Client("cloud_subscriber")
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/pi/#")
Run on:

Same Pi using two terminals OR

Two different Raspberry Pis or laptops across networks

🔍 Test from a Laptop / Mobile Phone
Use a web MQTT client like:

HiveMQ Web Client

MQTT Explorer

Connect to broker.hivemq.com:1883

Subscribe to your topic (iot/pi/#)

See the live data from your Pi publisher!



-----------------------------------------------------------------------
📋 Assignment 4
🧪 Objective:
Publish temperature/pressure to a public MQTT broker, and view on another device/network.




✍️ Instructions:
Modify your MQTT publisher to connect to broker.hivemq.com or test.mosquitto.org

Publish BMP280 sensor data every 10 seconds to a topic like:

iot/classroom/raspi01
On another device (laptop, Pi, mobile):

Run the subscriber script or use HiveMQ web client

Subscribe to iot/classroom/# and verify live sensor data