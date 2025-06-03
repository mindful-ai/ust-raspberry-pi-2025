from gpiozero import LED, Button

class GPIOInterface:

    def __init__(self):
        self.led = LED(26)
        self.button = Button(20) 
        self.led_state = False

    def toggle_led(self):
        if self.led_state:
            self.led.off()
        else:
            self.led.on()
        self.led_state = not self.led_state

    def is_key_pressed(self):
        return self.button.is_pressed