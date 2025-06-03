import smbus2
import time

class BMP280:
    def __init__(self, bus=1, address=0x76):
        self.bus = smbus2.SMBus(bus)
        self.address = address
        self._load_calibration_data()
        self._configure_sensor()

    def _load_calibration_data(self):
        # Read 24 bytes of calibration data
        cal = self.bus.read_i2c_block_data(self.address, 0x88, 24)
        self.dig_T1 = cal[1] << 8 | cal[0]
        self.dig_T2 = self._to_signed(cal[3] << 8 | cal[2])
        self.dig_T3 = self._to_signed(cal[5] << 8 | cal[4])
        # Only temp calibration for brevity
        self.t_fine = 0

    def _configure_sensor(self):
        # Set temp oversampling x1, normal mode
        self.bus.write_byte_data(self.address, 0xF4, 0x27)
        self.bus.write_byte_data(self.address, 0xF5, 0xA0)

    def _to_signed(self, n):
        return n - 65536 if n > 32767 else n

    def read_temperature(self):
        # Read raw temp data (20-bit)
        data = self.bus.read_i2c_block_data(self.address, 0xFA, 3)
        raw_temp = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        
        # Compensate temperature
        var1 = (((raw_temp >> 3) - (self.dig_T1 << 1)) * self.dig_T2) >> 11
        var2 = (((((raw_temp >> 4) - self.dig_T1) * ((raw_temp >> 4) - self.dig_T1)) >> 12) * self.dig_T3) >> 14
        self.t_fine = var1 + var2
        temp = (self.t_fine * 5 + 128) >> 8
        return temp / 100.0

if __name__ == "__main__":
    sensor = BMP280()
    while True:
        temp = sensor.read_temperature()
        print(f"Temperature: {temp:.2f} °C")
        time.sleep(1)
