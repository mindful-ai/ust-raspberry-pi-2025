import  adafruit_bmp280
import time, busio, board

# create a bus interface object
i2c = busio.I2C(board.SCL, board.SDA)

# create the sensor object
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# read the data
print("BMP280 Sensor Readings")
print("------------------------------------")

temp = bmp280.temperature
pres = bmp280.pressure
alti = bmp280.altitude


print("Temperature  -> ", temp)
print("Pressure     -> ", pres)
print("Altitude     -> ", alti)
print()
