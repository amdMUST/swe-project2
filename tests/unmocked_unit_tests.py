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
from py_files.city import city_manager

INPUT = "INPUT"
EXPECTED_OUTPUT = "EXPECTED_OUTPUT"

class VerifyCityName(unittest.TestCase):
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

# class UnitTest2(unittest.TestCase):
#     def setUp(self):
#         self.success_test_params = [
#             {
#                 INPUT: ("LONDON\nPARIS\nNEW YORK"),
#                 EXPECTED_OUTPUT: ["LONDON", "PARIS", "NEW YORK"],
#             },
#             {
#                 INPUT: (""),
#                 EXPECTED_OUTPUT: [],
#             },
#             {
#                 INPUT: ("       LONDON    \n           PARIS       \n        NEW YORK       "),
#                 EXPECTED_OUTPUT: ["LONDON", "PARIS", "NEW YORK"],
#             },
#         ]

#     def test_getCity(self):
#         for test in self.success_test_params:
#             self.assertEqual(city_manager.get_city(test[INPUT]), test[EXPECTED_OUTPUT])

if __name__ == "__main__":
    unittest.main()