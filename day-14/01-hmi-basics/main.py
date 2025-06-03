import tkinter as tk
from hardware.gpio_interface import GPIOInterface

class PioneerHMI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pioneer HMI")

        self.gpio = GPIOInterface()

        # LED Controls
        self.led_status = tk.StringVar(value="OFF")
        tk.Label(root, text="LED Control (GPIO26)", font=("Arial", 12)).pack()
        self.led_btn = tk.Button(root, text="Toggle LED", command=self.toggle_led, width=20)
        self.led_btn.pack(pady=5)
        self.led_label = tk.Label(root, textvariable=self.led_status, fg="blue", font=("Arial", 10))
        self.led_label.pack()

        # Key Press Status
        tk.Label(root, text="KEY Press Status", font=("Arial", 12)).pack(pady=10)
        self.key_status = tk.StringVar(value="Released")
        self.key_label = tk.Label(root, textvariable=self.key_status, fg="green", font=("Arial", 10))
        self.key_label.pack()      

        # Periodic Update
        self.update_status()


    def toggle_led(self):
        self.gpio.toggle_led()
        self.led_status.set("ON" if self.gpio.led_state else "OFF")

    def update_status(self):
        if self.gpio.is_key_pressed():
            self.key_status.set("Pressed")
            self.key_label.config(fg="red")
        else:
            self.key_status.set("Released")
            self.key_label.config(fg="green")
        self.root.after(500, self.update_status)

if __name__ == "__main__":
    root = tk.Tk()
    app = PioneerHMI(root)
    root.mainloop()