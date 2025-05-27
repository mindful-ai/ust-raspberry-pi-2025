
from gpiozero import  PWMLED
from time import sleep

led = PWMLED(26)

try:
        while True:
                print("Fade-in starts...")
                for dc in range(0, 101, 5):
                        led.value = dc/100.0
                        sleep(0.1)
                print("Fade-out starts...")
                for dc in range(100, -1, -5):
                        led.value = dc/100.0
                        sleep(0.1)
except KeyboardInterrupt:
        print("Stopping ....")
        led.off()
