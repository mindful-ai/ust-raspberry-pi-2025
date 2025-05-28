from smbus2 import SMBus
import time

# I2C address of BMP280 (usually 0x76 or 0x77)
BMP280_I2C_ADDR = 0x76

# BMP280 Register addresses
REG_ID = 0xD0
REG_RESET = 0xE0
REG_CTRL_MEAS = 0xF4
REG_CONFIG = 0xF5
REG_PRESSURE_DATA = 0xF7
REG_TEMP_DATA = 0xFA
REG_CALIB_START = 0x88

# Oversampling settings
OSRS_T = 1  # Temperature oversampling x1
OSRS_P = 1  # Pressure oversampling x1
MODE = 3    # Normal mode

ctrl_meas = (OSRS_T << 5) | (OSRS_P << 2) | MODE

def read_unsigned_short(bus, addr):
    lsb = bus.read_byte_data(BMP280_I2C_ADDR, addr)
    msb = bus.read_byte_data(BMP280_I2C_ADDR, addr + 1)
    return (msb << 8) + lsb

def read_signed_short(bus, addr):
    result = read_unsigned_short(bus, addr)
    if result > 32767:
        result -= 65536
    return result

def read_calibration_params(bus):
    calib = {}
    calib['dig_T1'] = read_unsigned_short(bus, 0x88)
    calib['dig_T2'] = read_signed_short(bus, 0x8A)
    calib['dig_T3'] = read_signed_short(bus, 0x8C)
    calib['dig_P1'] = read_unsigned_short(bus, 0x8E)
    calib['dig_P2'] = read_signed_short(bus, 0x90)
    calib['dig_P3'] = read_signed_short(bus, 0x92)
    calib['dig_P4'] = read_signed_short(bus, 0x94)
    calib['dig_P5'] = read_signed_short(bus, 0x96)
    calib['dig_P6'] = read_signed_short(bus, 0x98)
    calib['dig_P7'] = read_signed_short(bus, 0x9A)
    calib['dig_P8'] = read_signed_short(bus, 0x9C)
    calib['dig_P9'] = read_signed_short(bus, 0x9E)
    return calib

def compensate_temp(adc_T, calib):
    var1 = (((adc_T >> 3) - (calib['dig_T1'] << 1)) * calib['dig_T2']) >> 11
    var2 = (((((adc_T >> 4) - calib['dig_T1']) * ((adc_T >> 4) - calib['dig_T1'])) >> 12) * calib['dig_T3']) >> 14
    t_fine = var1 + var2
    temp = (t_fine * 5 + 128) >> 8
    return temp / 100.0, t_fine

def compensate_pressure(adc_P, calib, t_fine):
    var1 = t_fine - 128000
    var2 = var1 * var1 * calib['dig_P6']
    var2 += (var1 * calib['dig_P5']) << 17
    var2 += calib['dig_P4'] << 35
    var1 = ((var1 * var1 * calib['dig_P3']) >> 8) + ((var1 * calib['dig_P2']) << 12)
    var1 = (((1 << 47) + var1) * calib['dig_P1']) >> 33
    if var1 == 0:
        return 0
    p = 1048576 - adc_P
    p = ((p << 31) - var2) * 3125 // var1
    var1 = (calib['dig_P9'] * (p >> 13) * (p >> 13)) >> 25
    var2 = (calib['dig_P8'] * p) >> 19
    pressure = ((p + var1 + var2) >> 8) + (calib['dig_P7'] << 4)
    return pressure / 25600.0

# Main loop
with SMBus(1) as bus:
    chip_id = bus.read_byte_data(BMP280_I2C_ADDR, REG_ID)
    print(f"BMP280 Chip ID: 0x{chip_id:X}")
    
    # Set control measurement register
    bus.write_byte_data(BMP280_I2C_ADDR, REG_CTRL_MEAS, ctrl_meas)

    # Read calibration data
    calib = read_calibration_params(bus)

    print("Reading sensor data...\n")
    while True:
        # Read raw temperature
        raw_temp = bus.read_i2c_block_data(BMP280_I2C_ADDR, REG_TEMP_DATA, 3)
        adc_T = (raw_temp[0] << 12) | (raw_temp[1] << 4) | (raw_temp[2] >> 4)

        # Read raw pressure
        raw_press = bus.read_i2c_block_data(BMP280_I2C_ADDR, REG_PRESSURE_DATA, 3)
        adc_P = (raw_press[0] << 12) | (raw_press[1] << 4) | (raw_press[2] >> 4)

        # Compensate temperature
        temp, t_fine = compensate_temp(adc_T, calib)

        # Compensate pressure
        pressure = compensate_pressure(adc_P, calib, t_fine)

        print(f"Temperature: {temp:.2f} °C")
        print(f"Pressure: {pressure:.2f} hPa")
        print("-" * 30)

        time.sleep(2)
