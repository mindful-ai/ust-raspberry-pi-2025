📋 Assignment 5
✍️ Objective:
Remotely control an LED on a Raspberry Pi using MQTT from another device or terminal.

💡 Instructions:
Connect an LED to GPIO17 of your Raspberry Pi.

Run the subscriber script to listen for commands on topic iot/pi/led.

On another device:

Write or use a simple publisher script to send "ON" or "OFF" via MQTT to the same topic.

OR use HiveMQ Web Client to manually publish "ON"/"OFF" to the topic.

Observe the LED changing state in real time.

🧪 Optional Enhancements:
Add command for TOGGLE or BLINK

Log received commands to a file with timestamp

Secure the broker communication using TLS or authentication