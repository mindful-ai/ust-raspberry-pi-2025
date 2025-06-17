
# 📘 Introduction to Device Tree on Linux (Raspberry Pi Focus)

## ✅ What is a Device Tree?

A **Device Tree** is a data structure for describing hardware. It is used by the **Linux kernel** to know what devices exist in a system, especially for **embedded devices** like Raspberry Pi.

### Why Is It Needed?
- Many embedded devices do not support automatic hardware discovery.
- Device Trees provide hardware details (like addresses, interrupts, and connections) that the OS needs to operate devices.

---

## 📦 Components of a Device Tree

| Component | Description |
|----------|-------------|
| Nodes    | Represent hardware components (e.g., `i2c@7e804000`) |
| Properties | Describe node characteristics (e.g., `reg = <0x7e804000 0x1000>;`) |
| Labels   | Optional names to reference nodes |

### Example Snippet:
```dts
i2c1: i2c@7e804000 {
    compatible = "brcm,bcm2835-i2c";
    reg = <0x7e804000 0x1000>;
    interrupts = <2 21>;
    status = "okay";
};
```

---

## ⚙️ How It’s Used

1. **Write `.dts`** (Device Tree Source)
2. **Compile to `.dtb`** (Device Tree Blob) using `dtc`
   ```bash
   dtc -I dts -O dtb -o mydevice.dtb mydevice.dts
   ```
3. **Deploy** via bootloader or `/boot/config.txt`

---

## 🧪 Common Raspberry Pi Usage

- Enabling/disabling I2C, SPI, UART, etc.
- Connecting sensors, GPIOs, and custom HATs
- Used in `/boot/config.txt` with lines like:
  ```ini
  dtoverlay=i2c-rtc,ds1307
  ```

---

## 🔍 Explore the Current Device Tree

```bash
ls /proc/device-tree/
dtc -I fs /proc/device-tree
```

---

## 📘 Example: Custom GPIO LED Device Tree Overlay

### 🧾 Step 1: Create the Overlay File (`gpio-led-overlay.dts`)

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

### 🛠 Step 2: Compile the Overlay

```bash
dtc -@ -I dts -O dtb -o gpio-led.dtbo gpio-led-overlay.dts
```

> Install `dtc` if needed:
```bash
sudo apt install device-tree-compiler
```

### 📁 Step 3: Move the `.dtbo` File

```bash
sudo cp gpio-led.dtbo /boot/overlays/
```

### ⚙️ Step 4: Enable in `/boot/config.txt`

```ini
dtoverlay=gpio-led
```

Then reboot:

```bash
sudo reboot
```

### ✅ Step 5: Control the LED

Check for LED:
```bash
ls /sys/class/leds/
```

Turn LED on:
```bash
echo 1 | sudo tee /sys/class/leds/status_led/brightness
```

Turn LED off:
```bash
echo 0 | sudo tee /sys/class/leds/status_led/brightness
```

---

## 🧠 Summary Table

| Step              | Task |
|-------------------|------|
| Create `.dts`     | Define the device |
| Compile `.dtbo`   | Use `dtc` |
| Copy to Boot      | Place in `/boot/overlays/` |
| Activate in Boot  | Modify `/boot/config.txt` |
| Test LED          | Use `/sys/class/leds/` |

---

## 💡 Tip

Other overlays (e.g., for SPI, I2C devices) work similarly. Raspberry Pi provides many in `/boot/overlays/`.
