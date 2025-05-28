🔍 Check Connected I2C Devices on Raspberry Pi
---------------------------------------------------------------------------------------------


Make sure I2C is enabled (sudo raspi-config > Interface Options > I2C → Enable), then run:


>sudo apt install -y i2c-tools
>i2cdetect -y 1

You’ll see something like:


     0 1 2 3 4 5 6 7 8 9 a b c d e f
00:          -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- 29 -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: 50 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- 77
This output would indicate:

0x29 → TCS34725 (Color sensor)
0x50 → EEPROM (AT24C08)
0x77 → BMP180 (Pressure sensor)

Installation of Required Libraries for BMP180
---------------------------------------------------------------------------------------------
Enable SPI and I2C
>sudo raspi-config

>sudo apt update
>sudo apt install -y python3-smbus i2c-tools
>pip install Adafruit-BMP

>i2cdetect -y 1
You should see 77 or something else listed in the grid.