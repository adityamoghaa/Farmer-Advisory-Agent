"""
Configuration module.
Loads environment variables from a .env file and exposes them as constants.
"""

import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

# Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# OpenWeatherMap API key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
