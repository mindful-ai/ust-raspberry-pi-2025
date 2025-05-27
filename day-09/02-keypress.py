
from gpiozero import Button
from time import sleep

button = Button(20,  pull_up=True)

print("Key press example")

try:

        while True:
                if button.is_pressed:
                        print("Button is pressed")
                        while button.is_pressed:
                                sleep(0.01)
                sleep(0.05)
except KeyboardInterrupt:
        print("\nProgram Terminated")