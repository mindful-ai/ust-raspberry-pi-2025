import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 1000))
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                chat_display.config(state='normal')
                chat_display.insert(tk.END, f"Server: {msg}\n")
                chat_display.config(state='disabled')
        except:
            break

def send_message():
    msg = message_var.get()
    if msg:
        client_socket.send(msg.encode())
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"You: {msg}\n")
        chat_display.config(state='disabled')
        message_var.set("")

# Tkinter UI
root = tk.Tk()
root.title("Client Chat Window")
chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_display.pack(padx=10, pady=10)

message_var = tk.StringVar()
entry = tk.Entry(root, textvariable=message_var, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
tk.Button(root, text="Send", command=send_message).pack(side=tk.LEFT, padx=10, pady=(0, 10))

threading.Thread(target=connect_to_server, daemon=True).start()
root.mainloop()


