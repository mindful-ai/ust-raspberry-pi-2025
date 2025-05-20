import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ServerChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Chat Window")

        self.chat_display = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.chat_display.pack(padx=10, pady=10)

        self.message_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.message_var, width=40)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5, pady=(0, 10))

        self.start_button = tk.Button(master, text="Start Server", command=self.start_server)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=(0, 10))

        self.stop_button = tk.Button(master, text="Stop Server", command=self.stop_server, state='disabled')
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=(0, 10))

        self.server_socket = None
        self.conn = None
        self.addr = None
        self.is_running = False

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("localhost", 1000))
        self.server_socket.listen(1)
        self.is_running = True
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Server started. Waiting for client...\n")
        self.chat_display.config(state='disabled')

        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')

        threading.Thread(target=self.accept_client, daemon=True).start()

    def accept_client(self):
        self.conn, self.addr = self.server_socket.accept()
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"Client connected: {self.addr}\n")
        self.chat_display.config(state='disabled')
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while self.is_running:
            try:
                msg = self.conn.recv(1024).decode()
                if msg:
                    self.chat_display.config(state='normal')
                    self.chat_display.insert(tk.END, f"Client: {msg}\n")
                    self.chat_display.config(state='disabled')
            except:
                break

    def send_message(self):
        msg = self.message_var.get()
        if msg and self.conn:
            try:
                self.conn.send(msg.encode())
                self.chat_display.config(state='normal')
                self.chat_display.insert(tk.END, f"You: {msg}\n")
                self.chat_display.config(state='disabled')
                self.message_var.set("")
            except:
                messagebox.showerror("Error", "Failed to send message")

    def stop_server(self):
        self.is_running = False
        if self.conn:
            try:
                self.conn.close()
            except:
                pass
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass

        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Server stopped.\n")
        self.chat_display.config(state='disabled')

        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerChatApp(root)
    root.mainloop()
