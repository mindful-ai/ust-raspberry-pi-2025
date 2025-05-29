import spidev
import lgpio
import time
from PIL import Image, ImageDraw, ImageFont

class SSD1306:
    def __init__(self, rst_pin, dc_pin, spi_bus=0, spi_device=0, width=128, height=64):
        self.rst_pin = rst_pin
        self.dc_pin = dc_pin
        self.width = width
        self.height = height
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 8000000
        self.spi.mode = 0b00
        self.chip = lgpio.gpiochip_open(0)
        lgpio.gpio_claim_output(self.chip, self.dc_pin)
        lgpio.gpio_claim_output(self.chip, self.rst_pin)
        self._reset()
        self._init_display()
        self.buffer = [0x00] * (self.width * self.height // 8)

    def _reset(self):
        lgpio.gpio_write(self.chip, self.rst_pin, 0)
        time.sleep(0.1)
        lgpio.gpio_write(self.chip, self.rst_pin, 1)
        time.sleep(0.1)

    def _write_command(self, cmd):
        lgpio.gpio_write(self.chip, self.dc_pin, 0)
        self.spi.writebytes([cmd])

    def _write_data(self, data):
        lgpio.gpio_write(self.chip, self.dc_pin, 1)
        self.spi.writebytes(data if isinstance(data, list) else [data])

    def _init_display(self):
        cmds = [
            0xAE, 0xD5, 0x80, 0xA8, 0x3F, 0xD3, 0x00, 0x40,
            0x8D, 0x14, 0x20, 0x00, 0xA1, 0xC8, 0xDA, 0x12,
            0x81, 0xCF, 0xD9, 0xF1, 0xDB, 0x40, 0xA4, 0xA6,
            0xAF
        ]
        for cmd in cmds:
            self._write_command(cmd)

    def image(self, image):
        image = image.convert('1')
        pixels = list(image.getdata())
        for page in range(0, self.height // 8):
            for x in range(self.width):
                byte = 0
                for bit in range(8):
                    y = page * 8 + bit
                    byte |= (0x01 << bit) if pixels[y * self.width + x] else 0
                self.buffer[page * self.width + x] = byte

    def show(self):
        for page in range(0, self.height // 8):
            self._write_command(0xB0 + page)
            self._write_command(0x00)
            self._write_command(0x10)
            start = page * self.width
            end = start + self.width
            self._write_data(self.buffer[start:end])

    def clear(self):
        self.buffer = [0x00] * (self.width * self.height // 8)
        self.show()

    def cleanup(self):
        self.clear()
        lgpio.gpiochip_close(self.chip)
        self.spi.close()

def draw_moving_square(disp, x_pos):
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    draw.rectangle((x_pos, 24, x_pos + 20, 44), outline=255, fill=255)
    draw.text((10, 0), "Moving Square", font=ImageFont.load_default(), fill=255)

    return image

def main():
    RST = 19
    DC = 16
    BUS = 0
    DEVICE = 0

    disp = SSD1306(rst_pin=RST, dc_pin=DC, spi_bus=BUS, spi_device=DEVICE)

    try:
        for x in range(0, disp.width - 20):
            img = draw_moving_square(disp, x)
            disp.image(img)
            disp.show()
            time.sleep(0.05)
        time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        disp.cleanup()

if __name__ == "__main__":
    main()
