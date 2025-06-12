
# 📸 Raspberry Pi Camera Setup Guide (CSI Interface)

## ✅ Prerequisites

- Raspberry Pi (with Bookworm OS or newer)
- Official Raspberry Pi Camera Module (CSI connector)
- Properly seated camera ribbon cable (blue side facing the Ethernet/USB ports)

---

## 🔧 1. Connect the Camera

1. Power off your Raspberry Pi.
2. Gently lift the plastic latch on the CSI camera port.
3. Insert the ribbon cable:
   - Blue side facing the Ethernet port.
   - Metal contacts facing the HDMI ports.
4. Push down the latch to secure the cable.
5. Power on the Pi.

---

## ⚙️ 2. Enable the Camera (No `raspi-config` in Bookworm)

With Raspberry Pi OS Bookworm, the legacy `raspi-config` camera toggle is removed. Instead:

1. Edit the boot config file:

    ```bash
    sudo nano /boot/firmware/config.txt
    ```

2. Add this line at the bottom:

    ```ini
    start_x=1
    camera_auto_detect=1
    ```

3. Save & exit (Ctrl+O, Enter, Ctrl+X).

---

## 🔄 3. Reboot

```bash
sudo reboot
```

---

## 📥 4. Install Required Packages

```bash
sudo apt update
sudo apt install -y libcamera-apps python3-picamera2
```

---

## 📷 5. Test the Camera

Take a picture:

```bash
libcamera-still -o test.jpg
```

Other tools:

- Take JPEG photo:

    ```bash
    libcamera-jpeg -o photo.jpg
    ```

- Preview video stream:

    ```bash
    libcamera-hello
    ```

---

## 🐍 6. Use Camera in Python with `picamera2`

```python
from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.start()
time.sleep(2)
picam2.capture_file("capture.jpg")
print("Image captured!")
```

Save as `capture.py`, then run:

```bash
python3 capture.py
```

---

## 🧪 7. Use with OpenCV

```python
import cv2
from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "BGR888"
picam2.configure("preview")
picam2.start()
time.sleep(1)

while True:
    frame = picam2.capture_array()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```

---

## 🧼 8. Troubleshooting Tips

| Issue | Solution |
|-------|----------|
| Camera not detected | Double-check ribbon cable and config file |
| `libcamera` not found | Install `libcamera-apps` |
| `picamera2` not found | Run `sudo apt install python3-picamera2` |
| Still not working | Run `vcgencmd get_camera` (legacy, but should say `supported=1`) |
