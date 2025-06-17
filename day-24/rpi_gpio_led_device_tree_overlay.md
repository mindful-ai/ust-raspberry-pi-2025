
# Raspberry Pi Custom Device Tree Overlay: GPIO LED Example

This guide walks through creating a custom Device Tree overlay to control an LED connected to a Raspberry Pi GPIO pin.

---

## ✅ Objective

- Control an LED connected to **GPIO 17** via `/sys/class/leds/` using a custom Device Tree overlay.

---

## 🧾 Step 1: Create the Overlay Source File

Save the following as `gpio-led-overlay.dts`:

```dts
/dts-v1/;
/plugin/;

/ {
    compatible = "brcm,bcm2835";

    fragment@0 {
        target-path = "/";
        __overlay__ {
            gpio_leds: leds {
                compatible = "gpio-leds";

                status_led {
                    label = "status_led";
                    gpios = <&gpio 17 0>;  // GPIO 17, active high
                    default-state = "off";
                };
            };
        };
    };
};
```

---

## 🛠 Step 2: Compile the Overlay

```bash
dtc -@ -I dts -O dtb -o gpio-led.dtbo gpio-led-overlay.dts
```

> 📦 If `dtc` is not installed:
```bash
sudo apt install device-tree-compiler
```

---

## 📁 Step 3: Move the Overlay to the Pi Boot Partition

```bash
sudo cp gpio-led.dtbo /boot/overlays/
```

---

## ⚙️ Step 4: Load the Overlay via `config.txt`

Edit `/boot/config.txt` and add:

```ini
dtoverlay=gpio-led
```

Then reboot:

```bash
sudo reboot
```

---

## ✅ Step 5: Verify LED in Userspace

Check the LED class:

```bash
ls /sys/class/leds/
```

Expected output:
```
status_led
```

Turn LED ON:

```bash
echo 1 | sudo tee /sys/class/leds/status_led/brightness
```

Turn LED OFF:

```bash
echo 0 | sudo tee /sys/class/leds/status_led/brightness
```

---

## 📘 Summary Table

| Step              | Task Description                                   |
|-------------------|----------------------------------------------------|
| Create `.dts`     | Define overlay source for GPIO 17 LED              |
| Compile to `.dtbo`| Use `dtc` to generate blob                         |
| Install           | Move `.dtbo` to `/boot/overlays/`                 |
| Activate          | Add `dtoverlay=gpio-led` to `/boot/config.txt`    |
| Control LED       | Use `/sys/class/leds/status_led/brightness`       |

---

## 🧠 Tip

You can create overlays for I2C, SPI, UART, sensors, and displays similarly by modifying the `.dts` accordingly.

