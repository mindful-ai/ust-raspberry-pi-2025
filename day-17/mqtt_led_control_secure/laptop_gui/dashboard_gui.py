# laptop_gui/dashboard_gui.py

import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from common import config
import ssl

PI_IDS = ["pi1", "pi2", "pi3", "pi4", "pi5"]
statuses = {pi: tk.StringVar(value="Unknown") for pi in PI_IDS}

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with RC:", rc)
    for pi in PI_IDS:
        client.subscribe(f"pi/{pi}/led/status")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    for pi in PI_IDS:
        if topic == f"pi/{pi}/led/status":
            statuses[pi].set(payload)

client = mqtt.Client()
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set(ca_certs=config.CA_CERT, cert_reqs=ssl.CERT_REQUIRED)
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, config.PORT, 60)
client.loop_start()

# GUI setup
root = tk.Tk()
root.title("Secure Pi LED Dashboard")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

for idx, pi in enumerate(PI_IDS):
    row = idx + 1
    ttk.Label(frame, text=pi.upper()).grid(row=row, column=0, padx=5, pady=5)
    ttk.Label(frame, textvariable=statuses[pi]).grid(row=row, column=1, padx=5)

    def make_callback(p=pi, state="ON"):
        return lambda: client.publish(f"pi/{p}/led/control", state)

    ttk.Button(frame, text="ON", command=make_callback(pi, "ON")).grid(row=row, column=2)
    ttk.Button(frame, text="OFF", command=make_callback(pi, "OFF")).grid(row=row, column=3)

root.mainloop()
