"""
Weather tool.
Fetches current weather data for a given city using the OpenWeatherMap API.
"""

import requests
from config import OPENWEATHER_API_KEY

# OpenWeatherMap current-weather endpoint
OWM_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Args:
        city: Name of the city (e.g. "Delhi").

    Returns:
        A human-readable string with temperature, humidity, and condition,
        or an error message on failure.
    """
    if not OPENWEATHER_API_KEY:
        return "[Error] OPENWEATHER_API_KEY is not set. Please add it to your .env file."

    try:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",  # Celsius
        }
        response = requests.get(OWM_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()

        return (
            f"Weather in {city}:\n"
            f"  • Temperature: {temp}°C\n"
            f"  • Humidity: {humidity}%\n"
            f"  • Condition: {condition}"
        )

    except requests.exceptions.HTTPError as e:
        return f"[Error] Weather API returned an error: {e}"
    except requests.exceptions.ConnectionError:
        return "[Error] Could not connect to the weather service. Check your internet connection."
    except requests.exceptions.Timeout:
        return "[Error] Weather API request timed out."
    except Exception as e:
        return f"[Error] Failed to fetch weather data: {str(e)}"
