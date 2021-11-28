import unittest
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from py_files.weather import weather_client
from py_files.nyt import nyt_client

INPUT = "INPUT"
EXPECTED_OUTPUT = "EXPECTED_OUTPUT"


class VerifyCityNameTest(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                INPUT: "",
                EXPECTED_OUTPUT: False,
            },
            {
                INPUT: None,
                EXPECTED_OUTPUT: False,
            },
            {
                INPUT: "Washington",
                EXPECTED_OUTPUT: True,
            },
        ]

    def test_VerifyCityName(self):
        client = weather_client()
        for test in self.success_test_params:
            self.assertEqual(client.verifyCity(test[INPUT]), test[EXPECTED_OUTPUT])


class getArticleTest(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                INPUT: (""),
                EXPECTED_OUTPUT: [
                    ("headlines", []),
                    ("abstract", []),
                    ("web_url", []),
                    ("img_url", []),
                    ("lead_paragraph", []),
                ],
            },
        ]
        self.failure_test_params = [
            {
                INPUT: (""),
                EXPECTED_OUTPUT: [
                    ("headlines", ["headline1", "headline2", "headline3", "headline4", "headline5"]),
                    ("abstract", ["abstract1", "abstract2", "abstract3", "abstract4", "abstract5"]),
                    ("web_url", ["web_url1", "web_url2", "web_url3", "web_url4", "web_url5"]),
                    ("img_url", ["img_url1", "img_url2", "img_url3", "img_url4", "img_url5"]),
                    ("lead_paragraph", ["lead_paragraph1", "lead_paragraph2", "lead_paragraph3", "lead_paragraph4", "lead_paragraph5"]),
                ],
            },
        ]

    def test_getArticle(self):
        # Do not assign values to the class and see if the null values are being returned from the function
        client = nyt_client()
        for test in self.success_test_params:
            self.assertEqual(client.getArticle(), test[EXPECTED_OUTPUT])

        # Assign values to the class and see if the new values are being returned from the function
        client.headlines = ["headline1", "headline2", "headline3", "headline4", "headline5"]
        client.abstract = ["abstract1", "abstract2", "abstract3", "abstract4", "abstract5"]
        client.web_url = ["web_url1", "web_url2", "web_url3", "web_url4", "web_url5"]
        client.img_url = ["img_url1", "img_url2", "img_url3", "img_url4", "img_url5"]
        client.lead_paragraph = ["lead_paragraph1", "lead_paragraph2", "lead_paragraph3", "lead_paragraph4", "lead_paragraph5"]
        for test in self.failure_test_params:
            self.assertEqual(client.getArticle(), test[EXPECTED_OUTPUT])


if __name__ == "__main__":
    unittest.main()
