import paho.mqtt.client as mqtt
import time


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "raspi_publisher")
#client = mqtt.Client("led_publisher")
client.connect("broker.hivemq.com", 1883, 60)

while True:
    cmd = input("Enter LED command (ON/OFF): ").strip().upper()
    if cmd in ["ON", "OFF"]:
        client.publish("iot/pi/led", cmd)
    else:
        print("Invalid command. Use ON or OFF.")
