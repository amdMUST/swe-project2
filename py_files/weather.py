# py file for OpenWeather api
import requests, json, os
from dotenv import load_dotenv, find_dotenv

# a class to handle all of the weather requests the web-app will make
class weather_client:
    def __init__(self):
        # configuration of variables
        self.weather_main = 'null'
        self.weather_desc = 'null'
        self.temp = 'null'
        self.feels_like = 'null'
        self.temp_min = 'null'
        self.temp_max = 'null'
        self.pressure = 'null'
        self.humidity = 'null'
        self.clouds = 'null'
        self.wind = 'null'

    def get_weather(self, city):

        # validate and make sure city exists and is in the right format
        if not self.verifyCity(city):
            return

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        API_KEY = os.environ.get('WEATHER_API_KEY')
        BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

        URL = BASE_URL + 'q=' + city + '&appid=' + API_KEY + '&units=imperial'

        try:
            response = requests.get(URL)
            data = json.loads(response.text)

            # parse out data from correct response
            self.weather_main = data["weather"][0]["main"]
            self.weather_desc = data["weather"][0]["description"]
            
            self.temp = data["main"]["temp"]
            self.feels_like = data["main"]["feels_like"]
            self.temp_min = data["main"]["temp_min"]
            self.temp_max = data["main"]["temp_max"]

            self.pressure = data["main"]["pressure"]
            self.humidity = data["main"]["humidity"]
            
            self.clouds = data["clouds"]["all"]
            self.wind = data["wind"]["speed"]
        except:
            # error 
            return 

    # function to verify the cities name is correct for the request
    def verifyCity(self, city):
        return True

    # function to turn serialize the class into json
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

if __name__ == "__main__":
    weather_client()