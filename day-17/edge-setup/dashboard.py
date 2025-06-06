import paho.mqtt.client as mqtt
import ssl
import tkinter as tk
from collections import defaultdict

BROKER = "broker.hivemq.com"
PORT = 1883
PI_IDS = [f"raspi{i}" for i in range(1, 6)]  # Replace with actual Pi hostnames

power_data = defaultdict(lambda: "Waiting...")
clients = {}

def create_gui():
    window = tk.Tk()
    window.title("IoT Power Monitor Dashboard")

    labels = {}
    for pi_id in PI_IDS:
        frame = tk.Frame(window)
        frame.pack(pady=5)
        tk.Label(frame, text=pi_id, width=20).pack(side=tk.LEFT)
        label = tk.Label(frame, text="-- W", width=10)
        label.pack(side=tk.LEFT)
        labels[pi_id] = label
        btn = tk.Button(frame, text="Reset", command=lambda i=pi_id: send_reset(i))
        btn.pack(side=tk.LEFT)

    def update_labels():
        for pi_id in PI_IDS:
            labels[pi_id].config(text=f"{power_data[pi_id]} W")
        window.after(1000, update_labels)

    update_labels()
    return window

def send_reset(pi_id):
    clients[pi_id].publish(f"power/{pi_id}/command", "RESET")
    print(f"[Dashboard] Sent RESET to {pi_id}")

def make_client(pi_id):
    client = mqtt.Client()
    #client.tls_set("mosquitto.org.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
    #client.tls_insecure_set(False)

    def on_connect(client, userdata, flags, rc):
        topic = f"power/{pi_id}/data"
        client.subscribe(topic)
        print(f"[Dashboard] Subscribed to {topic}")

    def on_message(client, userdata, msg):
        power_data[pi_id] = msg.payload.decode()

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_start()
    return client

for pi_id in PI_IDS:
    clients[pi_id] = make_client(pi_id)

app = create_gui()
app.mainloop()