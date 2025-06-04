Enable I2C on Raspberry Pi

sudo raspi-config
# Interfacing Options -> I2C -> Enable
sudo reboot


sudo apt-get update
sudo apt-get install python3-smbus i2c-tools
pip install paho-mqtt


i2cdetect -y 1
# Should show device at address 0x76 or 0x77

--------------------------------------------------------------------------

pip install bmp280
-> bmp_sensor.py

Publish Sensor Data over MQTT
-> mqtt_sensor_publisher.py

MQTT Subscriber to Visualize
-> mqtt_sensory_subscriber.py

---------------------------------------------------------------------------

Assignment:

📋 Assignment 3
📌 Task: Publish sensor data every 10 seconds and visualize in subscriber
Instructions:

Use the BMP280 sensor and bmp280_sensor.py module.

Write a script that:

Reads temperature and pressure.

Publishes to MQTT every 10 seconds.

Write a subscriber that:

Displays the data in the terminal.

💡 Optional Extension:

Save data to CSV.

Add timestamp in the payload.

Use json.dumps() to send structured payload.

JSON Structure:

import json
payload = json.dumps({
    "temperature": round(temperature, 2),
    "pressure": round(pressure, 2),
    "unit": "C/hPa",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
})
