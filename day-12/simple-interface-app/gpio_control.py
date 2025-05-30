from gpiozero import LED, Button

LED_PIN = 26
BUTTON_PIN = 20  # Adjust if needed

led = LED(LED_PIN)
button = Button(BUTTON_PIN, pull_up=True)  # pull_up=True since physical button likely pulls to ground

def toggle_led():
    if led.is_lit:
        led.off()
    else:
        led.on()

def get_led_status():
    return led.is_lit

def is_button_pressed():
    return button.is_pressed
