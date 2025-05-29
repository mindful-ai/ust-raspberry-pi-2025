
import socket

HOST = "0.0.0.0"     # Listen to all interfaces
PORT = 65432         # Choose beyond 1023

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        conn, addr = server.accept()
        with conn:
                print(f"[SERVER] Connected by {addr}")
                while True:
                        data = conn.recv(1024)
                        if not data:
                                break
                        print(f"[SERVER] Received: {data.decode()}")
                        message = input("-> ")
                        conn.sendall(message.encode())
