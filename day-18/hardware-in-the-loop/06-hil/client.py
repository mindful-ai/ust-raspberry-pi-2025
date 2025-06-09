# laptop/client.py
import socket
import json

PI_IP = "192.168.126.83"  # Replace with actual Raspberry Pi IP
PORT = 5005

def fetch_sensor_data():
    request = json.dumps({"command": "get_data"}).encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PI_IP, PORT))
        s.sendall(request)
        data = s.recv(1024)
        return json.loads(data.decode())