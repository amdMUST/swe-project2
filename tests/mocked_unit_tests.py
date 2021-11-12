import unittest
from unittest.mock import MagicMock, patch

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

from app import isUserInDB, UserDB

INPUT = "INPUT"
EXPECTED_OUTPUT = "EXPECTED_OUTPUT"

class isUserInDBTest(unittest.TestCase):
    def setUp(self):
        self.db_mock = [UserDB(user_id="1", email="test@email.com", name="test")]

    def test_isUserInDBTest(self):
        with patch("app.UserDB.query") as mock_query:
            mock_filtered = MagicMock()
            mock_filtered.all.return_value = self.db_mock
            mock_query.filter_by.return_value = mock_filtered

            # Now that setup is done...
            # 1) Check if ID is in the DB already. Should be True
            self.assertEqual(isUserInDB("1"), True)

            # 2) Check if ID is in the DB already. Should be False
            # # what the return value should be for the second assertion
            mock_filtered.all.return_value = ''
            mock_query.filter_by.return_value = mock_filtered
            self.assertEqual(isUserInDB("2"), False)


if __name__ == "__main__":
    unittest.main()