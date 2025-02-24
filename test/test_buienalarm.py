import unittest
from unittest.mock import patch, call
import sys
from io import StringIO

# Import the function from the original script
from buienalarm import open_safari

class TestBuienalarm(unittest.TestCase):

    @patch('subprocess.run')
    def test_open_safari_valid_location(self, mock_subprocess_run):
        locations = {
            "delft": "https://www.buienalarm.nl/nederland/delft/8569",
            "rotterdam": "https://www.buienalarm.nl/nederland/rotterdam/16707",
            "brussels": "https://www.buienalarm.nl/belgie/brussels/7196",
            "antwerp": "https://www.buienalarm.nl/belgie/antwerpen/5686",
        }

        for location, url in locations.items():
            mock_subprocess_run.reset_mock()
            result = open_safari(location)
            self.assertEqual(result, "OK")
            mock_subprocess_run.assert_called_once_with(["open", "-a", "Safari", url])

    @patch('subprocess.run')
    def test_open_safari_invalid_location(self, mock_subprocess_run):
        locations = {"ewdew","fw331//.rfw","pk\nfr","dwed🌧️we"}

        for location in locations:
            mock_subprocess_run.reset_mock()
            result = open_safari(location)
            self.assertEqual(result, "ERROR_INVALID_LOCATION")
            mock_subprocess_run.assert_not_called()

if __name__ == '__main__':
    unittest.main()