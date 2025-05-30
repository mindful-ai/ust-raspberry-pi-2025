import board
import busio
import adafruit_bmp280

# Create I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Optional: change sea level pressure (for accurate altitude, if needed)
bmp280.sea_level_pressure = 1013.25

def get_sensor_data():
    try:
        temperature = bmp280.temperature  # °C
        pressure = bmp280.pressure       # hPa

        return {
            "temperature_celsius": round(temperature, 2),
            "pressure_hpa": round(pressure, 2)
        }

    except Exception as e:
        return {"error": str(e)}
