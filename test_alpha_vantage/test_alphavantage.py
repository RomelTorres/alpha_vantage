from ..alpha_vantage.alphavantage import AlphaVantage
from ..alpha_vantage.timeseries import TimeSeries
from ..alpha_vantage.techindicators import TechIndicators
from ..alpha_vantage.sectorperformance import SectorPerformances
from ..alpha_vantage.cryptocurrencies import CryptoCurrencies
from ..alpha_vantage.foreignexchange import ForeignExchange
from pandas import DataFrame as df
import unittest
import mock
import sys
from os import path
import urllib


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

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_handle_api_call_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data = av._handle_api_call(url)
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2.7")
    @mock.patch('urllib.urlopen')
    def test_handle_api_call_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data = av._handle_api_call(url)
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_time_series_intraday_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_time_series_intraday_pandas_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2")
    @mock.patch('urllib.urlopen')
    def test_time_series_intraday_pandas_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_time_series_intraday_date_indexing_python3(self, mock_urlopen):
        """ Test that api call returns a pandas data frame with a date as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='date')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == str

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2")
    @mock.patch('urllib.urlopen')
    def test_time_series_intraday_date_indexing_python2(self, mock_urlopen):
        """ Test that api call returns a pandas data frame with a date as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='date')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == str

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_time_series_intraday_date_integer_python3(self, mock_urlopen):
        """ Test that api call returns a pandas data frame with an integer as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='integer')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == int

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2")
    @mock.patch('urllib.urlopen')
    def test_time_series_intraday_date_integer_python2(self, mock_urlopen):
        """ Test that api call returns a pandas data frame with an integer as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='integer')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == int

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python  2.7")
    @mock.patch('urllib.urlopen')
    def test_time_series_intraday_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_technical_indicator_sma_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2.7")
    @mock.patch('urllib.urlopen')
    def test_technical_indicator_sma_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_technical_indicator_sma_pandas_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2.7")
    @mock.patch('urllib.urlopen')
    def test_technical_indicator_sma_pandas_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_sector_perfomance_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        sp = SectorPerformances(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = sp.get_sector()
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python 2.7")
    @mock.patch('urllib.urlopen')
    def test_sector_perfomance_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        sp = SectorPerformances(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = sp.get_sector()
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_foreign_exchange_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = fe.get_currency_exchange_rate(
                from_currency='BTC', to_currency='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python  2.7")
    @mock.patch('urllib.urlopen')
    def test_foreign_exchange_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = fe.get_currency_exchange_rate(
                from_currency='BTC', to_currency='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 2, "Test valid for python 3")
    @mock.patch('urllib.request.urlopen')
    def test_crypto_currencies_python3(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=CNY&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = cc.get_digital_currency_intraday(
                symbol='BTC', market='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @unittest.skipIf(sys.version_info.major == 3, "Test valid for python  2.7")
    @mock.patch('urllib.urlopen')
    def test_crypto_currencies_python2(self, mock_urlopen):
        """ Test that api call returns a json file as requested
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=CNY&apikey=test"
        path_file = self.get_file_from_url(url)
        with open(path_file) as f:
            mock_urlopen.return_value = f
            data, _ = cc.get_digital_currency_intraday(
                symbol='BTC', market='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
