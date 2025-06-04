
🛠️ Hands-On Activity (20 min)

🔧 Install Mosquitto on Raspberry Pi

sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

🚀 Publish and Subscribe in Terminal (on same Pi or over LAN)

In Terminal 1 (subscriber):

mosquitto_sub -h localhost -t "test/topic"

In Terminal 2 (publisher):

mosquitto_pub -h localhost -t "test/topic" -m "Hello IoT World!"

💡 Try QoS example:

mosquitto_pub -h localhost -t "test/topic" -m "QoS message" -q 1


------------------------------------------------------------------------------------------------

📘 Assignment 1 (to be done individually or in pairs)

Title: MQTT Local Messaging

Objective: Set up a working MQTT broker and demonstrate successful message exchange.

Instructions:

    Install Mosquitto on Raspberry Pi or your system.

    Start a subscriber listening on topic "myhome/test".

    In a separate terminal, publish any message (e.g., "Hello MQTT!") to the same topic.

    Try publishing with QoS 0 and 1.

    (Optional) Create a bash alias or simple Python script to automate this.

