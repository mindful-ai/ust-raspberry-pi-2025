import requests

API_KEY = "235lksflafhjf"  # Replace with your actual key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    try:
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return f"Error: {data.get('message', 'Unknown error')}"

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        return f"🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n☁️ Condition: {condition.capitalize()}"
    except Exception as e:
        return f"Exception: {e}"
