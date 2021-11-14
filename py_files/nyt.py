import os, json, requests
from dotenv import load_dotenv, find_dotenv

# a class to handle all of the weather requests the web-app will make
class nyt_client:
    def __init__(self):
        # configuration of variables
        self.nyt_main = "null"
        self.headlines = "null"
        self.abstract = "null"
        self.img_url = "null"
        self.web_url = "null"
        self.lead_paragraph = "null"

    def get_article_data(self, city):

        # validate and make sure city exists and is in the right format
        if not self.verifyCity(city):
            return

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        API_KEY = os.environ.get("NYT_API_KEY")
        BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

        params = {
            "q": city,
            "api-key": API_KEY,
        }
        # URL = BASE_URL + "api-key=" + API_KEY + "&q=" + city
        try:
            response = requests.get(BASE_URL, params=params)
            # data = json.loads(response.text)
            data = response.json()
            article = data["response"]["docs"][0]

            # parse out data from correct response
            # self.nyt_main = article
            self.headlines = article["headline"]["main"]
            self.abstract = article["abstract"]
            self.img_url = article["multimedia"][1]["url"]
            self.web_url = article["web_url"]
            self.lead_paragraph = article["lead_paragraph"]

        except:
            print("error")
            return

    # function to verify the cities name is correct for the request
    def verifyCity(self, city):
        # check to make sure city isnt blank
        if not city:
            return False
        return True

    def getArticle(self):
        dict = [
            ("headlines", self.headlines),
            ("abstract", self.abstract),
            ("image_url", self.img_url),
            ("web_url", self.web_url),
            ("lead_paragraph", self.lead_paragraph),
        ]
        print(dict)
        return dict


if __name__ == "__main__":
    nyt_client()
