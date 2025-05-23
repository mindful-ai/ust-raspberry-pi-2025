import requests
from datetime import datetime
import random

API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "weather" not in data:
        return None  # Handle bad city names

    icon_code = data["weather"][0]["main"].lower()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"].capitalize()
    timestamp = datetime.now().strftime('%H:%M')

    return {
        "temp": temperature,
        "desc": description,
        "icon": icon_code,
        "time": timestamp
    }

def get_historical_data():
    return [random.uniform(15, 30) for _ in range(10)]
