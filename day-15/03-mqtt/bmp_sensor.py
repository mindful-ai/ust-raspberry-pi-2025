import smbus2
import bme280

# I2C address of BMP280 on Pioneer600
port = 1
address = 0x76   
bus = smbus2.SMBus(port)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

# Read sensor data
def read_bmp280():
    data = bme280.sample(bus, address, calibration_params)
    return data.temperature, data.pressure
