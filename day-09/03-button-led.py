
from gpiozero import LED, Button
from signal import pause


LED_PIN = 26
BUTTON_PIN = 20


led = LED(LED_PIN)
button = Button(BUTTON_PIN)


button.when_pressed = led.on
button.when_released = led.off


pause()