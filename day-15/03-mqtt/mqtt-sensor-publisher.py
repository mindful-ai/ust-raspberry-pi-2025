import time
import paho.mqtt.client as mqtt
from bmp280_sensor import read_bmp280

# client = mqtt.Client("BMP280_Publisher")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "BMP280_Publisher")
client.connect("localhost")  # Or IP of MQTT broker

while True:
    temperature, pressure = read_bmp280()
    payload = f"Temp: {temperature:.2f} C | Pressure: {pressure:.2f} hPa"
    client.publish("sensor/bmp280", payload)
    print("Published:", payload)
    time.sleep(5)
