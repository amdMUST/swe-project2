import os, json, requests
from dotenv import load_dotenv, find_dotenv

# a class to handle all of the weather requests the web-app will make
class nyt_client:
    def __init__(self):
        # configuration of variables
        self.nyt_main = "null"
        self.nyt_headlines = "null"
        self.nyt_abstract = "null"
        self.nyt_img_url = "null"
        self.nyt_web_url = "null"
        self.nyt_lead_paragraph = "null"
        # might not be needed
        self.returning_dict = "null"

    def get_article_data(self, city):

        # validate and make sure city exists and is in the right format
        if not self.verifyCity(city):
            return

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        API_KEY = os.environ.get("NYT_API_KEY")
        BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

        URL = BASE_URL + "api-key=" + API_KEY + "&q=" + city

        try:
            response = requests.get(URL)
            data = json.loads(response.text)
            article = data["response"]["docs"]

            # parse out data from correct response
            self.nyt_main = article
            self.nyt_headlines = article["headline"]["main"]
            self.nyt_abstract = article["abstract"]
            self.nyt_img_url = article["multimedia"][1]["url"]
            self.nyt_web_url = article["web_url"]
            self.nyt_lead_paragraph = article["lead_paragraph"]

            # might not be needed will check
            self.returning_dict = {
                "headlines": list(self.nyt_headlines),
                "abstract": list(self.nyt_abstract),
                "image_url": list(self.nyt_img_url),
                "web_url": list(self.nyt_web_url),
                "lead_p": list(self.nyt_lead_paragraph),
            }

        except:
            # error
            return

    # function to verify the cities name is correct for the request
    def verifyCity(self, city):
        return True

    # function to turn serialize the class into json
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


if __name__ == "__main__":
    nyt_client()
