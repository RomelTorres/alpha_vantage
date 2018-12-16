from ..alpha_vantage.alphavantage import AlphaVantage
from ..alpha_vantage.timeseries import TimeSeries
from ..alpha_vantage.techindicators import TechIndicators
from ..alpha_vantage.sectorperformance import SectorPerformances
from ..alpha_vantage.cryptocurrencies import CryptoCurrencies
from ..alpha_vantage.foreignexchange import ForeignExchange
from pandas import DataFrame as df
import unittest
import sys
from os import path
import requests
import requests_mock


class TestAlphaVantage(unittest.TestCase):

    _API_KEY_TEST = "test"
    _API_EQ_NAME_TEST = 'MSFT'

    @staticmethod
    def get_file_from_url(url):
        """
            Return the file name used for testing, found in the test data folder
            formed using the original url
        """
        tmp = url
        for ch in [':', '/', '.', '?', '=', '&', ',']:
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

    @requests_mock.Mocker()
    def test_handle_api_call(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data = av._handle_api_call(url)
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')


    @requests_mock.Mocker()
    def test_time_series_intraday(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_time_series_intraday_pandas(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')


    @requests_mock.Mocker()
    def test_time_series_intraday_date_indexing(self, mock_request):
        """ Test that api call returns a pandas data frame with a date as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='date')
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            if sys.version_info[0] == 3:
                assert isinstance(data.index[0], str)
            else:
                assert isinstance(data.index[0], basestring)

    @requests_mock.Mocker()
    def test_time_series_intraday_date_integer(self, mock_request):
        """ Test that api call returns a pandas data frame with an integer as index
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas', indexing_type='integer')
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == int

    @requests_mock.Mocker()
    def test_technical_indicator_sma_python3(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url("mock_technical_indicator")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_technical_indicator_sma_pandas(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        url = "http://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url("mock_technical_indicator")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ti.get_sma("MSFT", interval='15min',
                                 time_period=10, series_type='close')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @requests_mock.Mocker()
    def test_sector_perfomance_python3(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        sp = SectorPerformances(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url("mock_sector")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = sp.get_sector()
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_sector_perfomance_pandas(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        sp = SectorPerformances(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        url = "http://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url("mock_sector")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = sp.get_sector()
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @requests_mock.Mocker()
    def test_foreign_exchange(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=test"
        path_file = self.get_file_from_url("mock_foreign_exchange")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = fe.get_currency_exchange_rate(
                from_currency='BTC', to_currency='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_crypto_currencies(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=CNY&apikey=test"
        path_file = self.get_file_from_url("mock_crypto_currencies")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = cc.get_digital_currency_intraday(
                symbol='BTC', market='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_crypto_currencies_pandas(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        cc = CryptoCurrencies(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        url = "http://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=CNY&apikey=test"
        path_file = self.get_file_from_url("mock_crypto_currencies")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = cc.get_digital_currency_intraday(
                symbol='BTC', market='CNY')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')

    @requests_mock.Mocker()
    def test_batch_quotes(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        url = "http://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=MSFT,FB,AAPL&apikey=test"
        path_file = self.get_file_from_url("mock_batch_quotes")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_batch_stock_quotes(symbols=('MSFT', 'FB', 'AAPL'))
            self.assertIsInstance(
                data[0], dict, 'Result Data must be a json dictionary')

    @requests_mock.Mocker()
    def test_batch_quotes_pandas(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        url = "http://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=MSFT,FB,AAPL&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_batch_quotes")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_batch_stock_quotes(symbols=('MSFT', 'FB', 'AAPL'))
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas dataframe')

