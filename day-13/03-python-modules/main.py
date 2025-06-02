# main.py

import time
from customlib import (
    get_simulated_temperature,
    get_simulated_humidity,
    get_simulated_pressure,
    log_to_file,
    check_thresholds
)

LOG_FILE = "sensor_log.txt"

def main():
    for i in range(5):
        temp = get_simulated_temperature()
        humid = get_simulated_humidity()
        pressure = get_simulated_pressure()

        print(f"Reading {i+1}: Temp = {temp} °C, Humidity = {humid} %, Pressure = {pressure} hPa")

        result = check_thresholds(temp, humid, pressure)
        if result['temperature_exceeded']:
            print("⚠️ Temperature exceeds threshold!")
        if result['humidity_exceeded']:
            print("⚠️ Humidity exceeds threshold!")
        if result['pressure_low']:
            print("⚠️ Pressure is unusually low!")
        if result['pressure_high']:
            print("⚠️ Pressure is unusually high!")

        log_to_file(LOG_FILE, temp, humid, pressure)
        time.sleep(1)

if __name__ == "__main__":
    main()
