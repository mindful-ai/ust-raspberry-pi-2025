import socket

SERVER_IP = '192.168.126.83'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect((SERVER_IP, PORT))
    print(f"[CLIENT] Connected to {SERVER_IP}:{PORT}")

    while True:

        message = input("-> ")
        if message == "!":
            break
        client.send(message.encode())
        data = client.recv(1024)
        print(f"[CLIENT] Received from server: {data.decode()}")