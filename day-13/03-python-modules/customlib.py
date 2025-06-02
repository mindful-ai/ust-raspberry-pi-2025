# customlib.py

import random
from datetime import datetime

def get_simulated_temperature(min_temp=20.0, max_temp=35.0):
    """Simulate a temperature reading."""
    return round(random.uniform(min_temp, max_temp), 2)

def get_simulated_humidity(min_humid=30.0, max_humid=80.0):
    """Simulate a humidity reading."""
    return round(random.uniform(min_humid, max_humid), 2)

def get_simulated_pressure(min_press=980.0, max_press=1050.0):
    """Simulate an atmospheric pressure reading in hPa."""
    return round(random.uniform(min_press, max_press), 2)

def log_to_file(filename, temperature, humidity, pressure):
    """Append sensor data to a log file with timestamp."""
    with open(filename, 'a') as file:
        timestamp = datetime.now().isoformat()
        file.write(f"{timestamp}, {temperature}, {humidity}, {pressure}\n")

def check_thresholds(temperature, humidity, pressure, 
                     temp_thresh=30.0, humid_thresh=70.0, press_thresh=(990, 1030)):
    """Check whether temperature, humidity or pressure exceed thresholds."""
    return {
        'temperature_exceeded': temperature > temp_thresh,
        'humidity_exceeded': humidity > humid_thresh,
        'pressure_low': pressure < press_thresh[0],
        'pressure_high': pressure > press_thresh[1]
    }
