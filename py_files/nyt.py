import os, json, requests
from dotenv import load_dotenv, find_dotenv

# a class to handle all of the weather requests the web-app will make
class nyt_client:
    def __init__(self):

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        self.API_KEY = os.environ.get("NYT_API_KEY")

        # configuration of variables
        self.nyt_main = ""
        self.headlines = ""
        self.abstract = ""
        self.img_url = ""
        self.web_url = ""
        self.lead_paragraph = ""

    def get_article_data(self, city):

        # validate and make sure city exists and is in the right format
        if not self.verifyCity(city):
            return

        # retrieve key and url for request
        load_dotenv(find_dotenv())
        API_KEY = os.environ.get("NYT_API_KEY")
        BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

        try:

            params = {
                "q": city,
                "api-key": API_KEY,
            }
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            articles = data["response"]["docs"]

            def get_headline(article):
                return article["headline"]["main"]

            def get_abstract(article):
                return article["abstract"]

            def get_img_url(article):
                image = ""
                try:
                    image = "https://www.nytimes.com/" + article["multimedia"][0]["url"]
                except:
                    image = "http://www.clipartbest.com/cliparts/dc7/pE6/dc7pE6Rpi.png"
                return image

            # TypeError: list indices must be integers or slices, not str
            def get_web_url(article):
                return article["web_url"]

            def get_lead_paragraph(article):
                return article["lead_paragraph"]

            self.headlines = map(get_headline, articles)
            self.abstract = map(get_abstract, articles)
            self.web_url = map(get_web_url, articles)
            self.img_url = map(get_img_url, articles)
            self.lead_paragraph = map(get_lead_paragraph, articles)
        except:
            print("nyt parsing error")
            return

    # function to verify the cities name is correct for the request
    def verifyCity(self, city):
        # check to make sure city isnt blank
        if not city:
            return False
        return True

    def getArticle(self):
        dict = [
            ("headlines", list(self.headlines)),
            ("abstract", list(self.abstract)),
            ("web_url", list(self.web_url)),
            ("img_url", list(self.img_url)),
            ("lead_paragraph", list(self.lead_paragraph)),
        ]
        return dict


if __name__ == "__main__":
    nyt_client()
