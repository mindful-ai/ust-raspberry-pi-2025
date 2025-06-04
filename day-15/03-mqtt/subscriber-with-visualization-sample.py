import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import re

# MQTT settings
broker_address = "localhost"
topic = "sensor/bmp280"

# Data storage (deque for sliding window plot)
max_points = 20
temps = deque(maxlen=max_points)
pressures = deque(maxlen=max_points)
timestamps = deque(maxlen=max_points)

# Message handler
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"[RECEIVED] {payload}")

    # Extract temperature and pressure using regex
    match = re.search(r"Temperature: ([\d.]+) C, Pressure: ([\d.]+) hPa", payload)
    if match:
        temp = float(match.group(1))
        pressure = float(match.group(2))

        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')

        temps.append(temp)
        pressures.append(pressure)
        timestamps.append(current_time)

# Set up MQTT client
# client = mqtt.Client(client_id="BMP280Subscriber", protocol=mqtt.MQTTv311)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "BMP280Subscriber")
client.connect(broker_address)
client.subscribe(topic)
client.on_message = on_message

# Setup for matplotlib animation
fig, ax1 = plt.subplots()
line1, = ax1.plot([], [], label='Temperature (°C)', color='tab:red')
ax1.set_ylim(15, 40)
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
line2, = ax2.plot([], [], label='Pressure (hPa)', color='tab:blue')
ax2.set_ylim(900, 1100)
ax2.set_ylabel('Pressure (hPa)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title("Real-Time Sensor Data")
plt.xlabel("Time")
fig.tight_layout()

def animate(i):
    line1.set_data(range(len(temps)), temps)
    line2.set_data(range(len(pressures)), pressures)
    ax1.set_xticks(range(len(timestamps)))
    ax1.set_xticklabels(timestamps, rotation=45, ha='right')
    ax1.set_xlim(0, len(timestamps) if timestamps else 10)
    return line1, line2

ani = animation.FuncAnimation(fig, animate, interval=1000)

# Start MQTT loop in background
client.loop_start()

plt.show()
