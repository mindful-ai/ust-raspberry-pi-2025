# OLED Display Guide for Waveshare Pioneer600

This guide explains how to use the SSD1306 OLED display on the Waveshare Pioneer600 board with a Raspberry Pi, via SPI.

## Requirements

* Raspberry Pi with SPI enabled
* Waveshare Pioneer600 OLED (128x64, SPI interface)
* Python3
* Libraries: `spidev`, `lgpio`, `Pillow`

Install required libraries:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install pillow spidev lgpio
```

## Wiring

Make sure the following connections are made:

* RST -> GPIO19
* DC  -> GPIO16
* SPI (MOSI, SCLK, CE0) -> connected to SPI0

## Code Explanation

### 1. Import Libraries

```python
import spidev
import lgpio
import time
from PIL import Image, ImageDraw, ImageFont
```

These libraries handle SPI communication, GPIO control, time delays, and image drawing.

### 2. Define `SSD1306` Display Class

The `SSD1306` class handles initialization, sending commands/data, managing image buffer, and showing content on the display.

#### `__init__()`

* Takes pin numbers and SPI configuration.
* Opens SPI and GPIO.
* Resets and initializes the display.

#### `_reset()`

* Sends a reset pulse to the display.

#### `_write_command()` and `_write_data()`

* Used to send command and data bytes via SPI.

#### `_init_display()`

* Sends a standard sequence of SSD1306 initialization commands.

#### `image()`

* Converts a `PIL.Image` to byte buffer format compatible with SSD1306.

#### `show()`

* Writes the buffer to the display one page at a time.

#### `cleanup()`

* Releases GPIO and SPI resources.

### 3. Setup Display

```python
RST = 19  # Reset pin
DC = 16   # Data/Command pin
bus = 0
device = 0

disp = SSD1306(rst_pin=RST, dc_pin=DC, spi_bus=bus, spi_device=device)
```

Initialize the display with the correct pins and SPI configuration.

### 4. Draw Content

```python
image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, disp.width, disp.height), fill=0)
```

* Create a blank monochrome image.
* Clear it by drawing a black rectangle.

### 5. Add Text

```python
font = ImageFont.load_default()
draw.text((0, 0), "Waveshare OLED", font=font, fill=255)
...
```

Draw multiple lines of text using the default font.

### 6. Display Image

```python
disp.image(image)
disp.show()
```

Convert the drawn image to SSD1306 format and show it.

### 7. Cleanup

```python
time.sleep(5)
disp.cleanup()
```

Pause for 5 seconds to view the display, then release resources.

## Summary

This script provides a basic implementation to control the OLED display on the Pioneer600 using Python. You can extend it to show dynamic data such as sensor readings or time.
