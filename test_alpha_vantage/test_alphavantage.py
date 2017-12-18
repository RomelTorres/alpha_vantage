from ..alpha_vantage.alphavantage import AlphaVantage
from pandas import DataFrame as df
import unittest
import mock
from os import path


class TestAlphaVantage(unittest.TestCase):

    _API_KEY_TEST = "test"
    _API_EQ_NAME_TEST = 'MSFT'

    @staticmethod
    def get_file_from_url(url):
        """
            Return the file name used for testing, found in the test data folder
            formed using the orginal url
        """
        tmp = url
        for ch in [':', '/', '.', '?', '=', '&']:
            if ch in tmp:
                tmp = tmp.replace(ch, '_')
        path_dir = path.join(path.dirname(
            path.abspath(__file__)), 'test_data/')
        return path.join(path.join(path_dir, tmp))

    def test_key_none(self):
        """Raise an error when a key has not been given
        """
        try:
            AlphaVantage()
            self.fail(msg='A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    @mock.patch('urllib.request.urlopen')
    def test_handle_api_call(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data = av._handle_api_call(url)
            print(data)
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
