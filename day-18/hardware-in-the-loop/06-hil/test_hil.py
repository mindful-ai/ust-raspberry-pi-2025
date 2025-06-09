# laptop/test_hil.py
import pytest
from client import fetch_sensor_data

def test_temperature_range():
    data = fetch_sensor_data()
    assert 20.0 <= data["temperature"] <= 50.0, f"Unexpected temperature: {data['temperature']}"

def test_pressure_range():
    data = fetch_sensor_data()
    assert 850.0 <= data["pressure"] <= 1100.0, f"Unexpected pressure: {data['pressure']}"