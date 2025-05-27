# Button Press Duration Demo on Raspberry Pi 5

This example demonstrates how to measure how long a button is pressed using the `gpiozero` library on a Raspberry Pi 5 running Bookworm OS.

---

## 🧪 Goal

Detect a button press and display how long it was held in seconds.

---

## 📦 Requirements

- Raspberry Pi 5
- Bookworm OS
- Python 3
- `gpiozero` library (Install with `sudo apt install python3-gpiozero`)
- Button connected to **GPIO26** 

---

## ⚡ Circuit Setup

- One leg of the push button connected to GPIO26
- The other leg connected to GND
- Enable internal pull-up with `pull_up=True` in code

---

## 🧠 Python Code

```python
from gpiozero import Button
import time

# Setup: Button connected to GPIO17
button = Button(26, pull_up=True)

print("Press and hold the button...")

try:
    while True:
        # Wait for button press
        button.wait_for_press()
        start_time = time.time()
        print("Button pressed.")

        # Wait for button release
        button.wait_for_release()
        duration = time.time() - start_time
        print(f"Button was held for {duration:.2f} seconds.\n")

except KeyboardInterrupt:
    print("\nProgram stopped.")
```

---

## ▶️ Running the Code

1. Save the code to a file, e.g., `button_duration.py`
2. Run it with:
   ```bash
   python button_duration.py
   ```
3. Press and hold the button to see the result.

---

## 📌 Notes

- Adjust GPIO pin number if using a different pin.
- This can be extended to control LEDs, trigger events, or log durations.

