#! /usr/bin/env python
from ..alpha_vantage.alphavantage import AlphaVantage
from ..alpha_vantage.timeseries import TimeSeries
from ..alpha_vantage.techindicators import TechIndicators
from ..alpha_vantage.sectorperformance import SectorPerformances
from ..alpha_vantage.foreignexchange import ForeignExchange
from ..alpha_vantage.fundamentaldata import FundamentalData

from pandas import DataFrame as df, Timestamp

import unittest
import sys
from os import path
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
    def test_rapidapi_key(self, mock_request):
        """ Test that the rapidAPI key calls the rapidAPI endpoint
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST, rapidapi=True)
        url = "https://alpha-vantage.p.rapidapi.com/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_time_series_intraday(self, mock_request):
        """ Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
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
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
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
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            if ts.indexing_type == 'date':
                assert isinstance(data.index[0], Timestamp)
            else:
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
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
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
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
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
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
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
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
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
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
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
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=test"
        path_file = self.get_file_from_url("mock_foreign_exchange")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = fe.get_currency_exchange_rate(
                from_currency='BTC', to_currency='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')

    @requests_mock.Mocker()
    def test_fundamental_data(self, mock_request):
        """Test that api call returns a json file as requested
        """
        fd = FundamentalData(key=TestAlphaVantage._API_KEY_TEST)
        url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=test'
        path_file = self.get_file_from_url("mock_fundamental_data")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = fd.get_income_statement_annual(symbol='IBM')
            self.assertIsInstance(data, df, 'Result Data must be a pandas data frame')

    @requests_mock.Mocker()
    def test_company_overview(self, mock_request):
        """Test that api call returns a json file as requested
        """
        fd = FundamentalData(key=TestAlphaVantage._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=test"
        path_file = self.get_file_from_url("mock_company_overview")
        with open(path_file) as f:
            mock_request.get(url, text=f.read())
            data, _ = fd.get_company_overview(symbol='IBM')
            self.assertIsInstance(data, dict, 'Result Data must be a dictionary')