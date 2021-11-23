# UNSPLASH city image request for given city.

import os, json, requests
from dotenv import load_dotenv, find_dotenv


class cityimg_client:
    def __init__(self):
        # configuration of variables
        self.img_url = "null"

    def get_cityimg_url(self, city):

        # validate and make sure city exists and is in the right format
        if not self.verifyCity(city):
            return

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
        BASE_URL = "https://api.unsplash.com/search/photos?query="

        params = {
            "query": city,
            "client_id": UNSPLASH_ACCESS_KEY,
        }

        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            self.img_url = data["results"][0]["urls"]["raw"]
        except:
            print("parsing error")
            return

    # function to verify the cities name is correct for the request
    def verifyCity(self, city):
        # check to make sure city isnt blank
        if not city:
            return False
        return True

    def getCityImg(self):
        dict = [
            ("image_url", self.img_url),
        ]
        return dict


if __name__ == "__main__":
    cityimg_client()
