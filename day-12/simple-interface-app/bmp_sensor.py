import board
import busio
import adafruit_bmp280

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
bmp280.sea_level_pressure = 1013.25

def get_sensor_data():
    try:
        return {
            "temperature": round(bmp280.temperature, 2),
            "pressure": round(bmp280.pressure, 2)
        }
    except Exception as e:
        return {"error": str(e)}
