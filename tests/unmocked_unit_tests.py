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
                    ("headlines", "null"),
                    ("abstract", "null"),
                    ("image_url", "null"),
                    ("web_url", "null"),
                    ("lead_paragraph", "null"),
                ],
            },
        ]
        self.failure_test_params = [
            {
                INPUT: (""),
                EXPECTED_OUTPUT: [
                    ("headlines", "test headline"),
                    ("abstract", "test abstract"),
                    ("image_url", "test image_url"),
                    ("web_url", "test web_url"),
                    ("lead_paragraph", "test lead_paragraph"),
                ],
            },
        ]

    def test_getArticle(self):
        # Do not assign values to the class and see if the null values are being returned from the function
        client = nyt_client()
        # for test in self.success_test_params:
        #     self.assertEqual(client.getArticle(), test[EXPECTED_OUTPUT])

        # Assign values to the class and see if the new values are being returned from the function
        client.headlines = "test headline"
        client.abstract = "test abstract"
        client.img_url = "test image_url"
        client.web_url = "test web_url"
        client.lead_paragraph = "test lead_paragraph"
        for test in self.failure_test_params:
            self.assertEqual(client.getArticle(), test[EXPECTED_OUTPUT])

if __name__ == "__main__":
    unittest.main()