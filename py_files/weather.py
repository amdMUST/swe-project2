# py file for OpenWeather api
import requests, json, os
from dotenv import load_dotenv, find_dotenv

# get the Database URL and change it to postgresql if needed
load_dotenv(find_dotenv())
API_KEY = os.environ.get('WEATHER_API_KEY')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
CITY = ''