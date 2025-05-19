from gpiozero import LED, Button
from signal import pause

led = LED(26)        # GPIO26
button = Button(20)  # GPIO20

def toggle_led():
    led.toggle()
    print("LED is now", "ON" if led.is_lit else "OFF")

button.when_pressed = toggle_led

print("Press the button to toggle the LED.")
pause()


--------------------------------------------------------------------

#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>

#define CHIPNAME "gpiochip4"   // Change if needed (run `gpiodetect`)
#define LED_PIN 26
#define BTN_PIN 20

volatile int keep_running = 1;

void handle_sigint(int sig) {
    keep_running = 0;
}

int main() {
    struct gpiod_chip *chip;
    struct gpiod_line *led, *btn;
    int led_state = 0, prev_btn = 1;

    signal(SIGINT, handle_sigint); // Handle Ctrl + C

    chip = gpiod_chip_open_by_name(CHIPNAME);
    if (!chip) {
        perror("Open chip failed");
        return 1;
    }

    led = gpiod_chip_get_line(chip, LED_PIN);
    btn = gpiod_chip_get_line(chip, BTN_PIN);
    gpiod_line_request_output(led, "led", 0);
    gpiod_line_request_input(btn, "button");

    printf("Press the button to toggle the LED (Ctrl+C to quit)\n");

    while (keep_running) {
        int btn_val = gpiod_line_get_value(btn);

        if (btn_val == 0 && prev_btn == 1) {  // Button pressed (falling edge)
            led_state = !led_state;
            gpiod_line_set_value(led, led_state);
            printf("LED is now %s\n", led_state ? "ON" : "OFF");
            usleep(200000); // debounce
        }

        prev_btn = btn_val;
        usleep(10000);
    }

    gpiod_line_release(led);
    gpiod_line_release(btn);
    gpiod_chip_close(chip);
    return 0;
}
