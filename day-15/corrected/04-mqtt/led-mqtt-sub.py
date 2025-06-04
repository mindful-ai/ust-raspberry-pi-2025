from gpiozero import LED
import paho.mqtt.client as mqtt

# Setup LED using gpiozero
led = LED(26)  # GPIO 26

# MQTT callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("iot/pi/led")

def on_message(client, userdata, msg):
    command = msg.payload.decode().strip().upper()
    print(f"Received command: {command}")
    if command == "ON":
        led.on()
    elif command == "OFF":
        led.off()

# MQTT setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "raspi_publisher")

#client = mqtt.Client("led_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()

