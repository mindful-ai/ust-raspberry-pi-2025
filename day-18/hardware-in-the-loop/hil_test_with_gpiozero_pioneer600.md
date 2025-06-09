
# 🔁 Hardware-in-the-Loop (HIL) Testing on Raspberry Pi with gpiozero and Pioneer600 HAT

## 🧠 What is Hardware-in-the-Loop (HIL) Testing?

**Hardware-in-the-Loop (HIL)** testing is a technique used to validate embedded systems and software by connecting them to real hardware components. This allows developers to:

- Simulate real-world conditions.
- Test hardware control logic.
- Identify integration issues early.

In an embedded Linux context (like Raspberry Pi), HIL enables interaction between your Python scripts and GPIO hardware (LEDs, sensors, motors, etc.) during automated testing.

---

## 🎯 Objective

Set up a HIL test on a **Raspberry Pi 5** running **Bookworm OS** using the **gpiozero** library and the **Pioneer600 HAT** from Waveshare. 

We will:

- Simulate a temperature reading.
- Control an onboard LED based on the temperature threshold.
- Verify GPIO state changes using `pytest`.

---

## 📦 Hardware Used

- Raspberry Pi 5
- Waveshare **Pioneer600 HAT**
- GPIO-connected LED (via Pioneer600)

---

## 📁 Folder Structure

```
hil_test_pioneer600/
├── app/
│   ├── monitor.py         # Core logic
│   └── hardware.py        # GPIOZero wrapper
├── test/
│   └── test_monitor.py    # HIL test with gpiozero
```

---

## 📜 `app/hardware.py` — GPIO Control via gpiozero

```python
from gpiozero import LED

# Pioneer600 has LEDs connected to GPIO17 (D1), GPIO18 (D2), etc.
LED_PIN = 26
led = LED(LED_PIN)

def set_led_state(state: bool):
    if state:
        led.on()
    else:
        led.off()

def get_led_state() -> bool:
    return led.is_lit
```

---

## 📜 `app/monitor.py` — Core Application Logic

```python
from app.hardware import set_led_state

TEMPERATURE_THRESHOLD = 30.0  # Celsius

def monitor_temperature(sensor_function):
    temp = sensor_function()
    set_led_state(temp > TEMPERATURE_THRESHOLD)
    return temp
```

---

## 📜 `test/test_monitor.py` — pytest HIL Test

```python
import pytest
from app import monitor, hardware

'''
This decorates the function as a pytest fixture. The autouse=True part means it runs automatically before and after every test in the module—no need to explicitly use it in test functions.
'''

@pytest.fixture(autouse=True)
def reset_led():
    hardware.set_led_state(False)
    yield
    hardware.set_led_state(False)

def test_led_on_high_temp():
    def fake_sensor():
        return 35.0

    result = monitor.monitor_temperature(fake_sensor)
    assert result == 35.0
    assert hardware.get_led_state() == True

def test_led_off_low_temp():
    def fake_sensor():
        return 25.0

    result = monitor.monitor_temperature(fake_sensor)
    assert result == 25.0
    assert hardware.get_led_state() == False
```

---

## 🧪 Running the Tests

```bash
sudo apt update
sudo apt install python3-gpiozero python3-pytest
cd hil_test_pioneer600
pytest
```

---

## 📌 Notes on Pioneer600

- Confirm LED pin numbers from the Waveshare Pioneer600 HAT documentation.
- Ensure the LEDs are properly powered and not inverted logic (some boards do this).
- Always use proper `GPIO.cleanup()` on other libraries — `gpiozero` manages it safely for you.

---

## ✅ Summary

| Feature                         | Purpose                                |
|----------------------------------|----------------------------------------|
| `gpiozero.LED` abstraction       | Clean, object-oriented GPIO control    |
| `pytest` fixture for cleanup     | Ensures GPIO state is reset            |
| Simulated temperature sensor     | Allows test automation                 |
| Real LED output as hardware loop | Confirms functional control logic      |

---

Happy Testing! 🧪🧡
