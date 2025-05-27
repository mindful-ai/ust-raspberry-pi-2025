from gpiozero import LED
from time import sleep

led = LED(26, active_high=False)

print("LED Experiment")

i = 0
while i < 20:
        try:
                led.on()
                sleep(1)
                led.off()
                sleep(1)
        except:
                print("There was an exception")
        i += 1
