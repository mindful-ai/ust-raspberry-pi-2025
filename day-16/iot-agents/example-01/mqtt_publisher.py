import paho.mqtt.publish as publish
import random
import time

MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "iot/device/temperature"

print("[Publisher] Starting temperature sensor simulation...")
while True:
    temp = round(random.uniform(20.0, 35.0), 2)
    publish.single(MQTT_TOPIC, str(temp), hostname=MQTT_BROKER)
    print(f"[Publisher] Sent temperature: {temp}°C")
    time.sleep(5)
 