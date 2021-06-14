#!/usr/bin/env python
from ..alpha_vantage.async_support.alphavantage import AlphaVantage
from ..alpha_vantage.async_support.timeseries import TimeSeries
from ..alpha_vantage.async_support.techindicators import TechIndicators
from ..alpha_vantage.async_support.sectorperformance import SectorPerformances
from ..alpha_vantage.async_support.foreignexchange import ForeignExchange

from pandas import DataFrame as df, Timestamp

import asyncio
from aioresponses import aioresponses
from functools import wraps
import json
from os import path
import unittest


def make_async(f):
    @wraps(f)
    def test_wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        asyncio.get_event_loop().run_until_complete(future)
    return test_wrapper


class TestAlphaVantageAsync(unittest.TestCase):
    """
    Async local tests for AlphaVantage components
    """
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
        """
        Raise an error when a key has not been given
        """
        try:
            AlphaVantage()
            self.fail(msg='A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    @make_async
    async def test_handle_api_call(self):
        """
        Test that api call returns a json file as requested
        """
        av = AlphaVantage(key=TestAlphaVantageAsync._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=test"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data = await av._handle_api_call(url)
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await av.close()

    @make_async
    async def test_rapidapi_key(self):
        """
        Test that the rapidAPI key calls the rapidAPI endpoint
        """
        ts = TimeSeries(key=TestAlphaVantageAsync._API_KEY_TEST, rapidapi=True)
        url = "https://alpha-vantage.p.rapidapi.com/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await ts.close()

    @make_async
    async def test_time_series_intraday(self):
        """
        Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantageAsync._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await ts.close()

    @make_async
    async def test_time_series_intraday_pandas(self):
        """
        Test that api call returns a json file as requested
        """
        ts = TimeSeries(key=TestAlphaVantageAsync._API_KEY_TEST,
                        output_format='pandas')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')
        await ts.close()

    @make_async
    async def test_time_series_intraday_date_indexing(self):
        """
        Test that api call returns a pandas data frame with a date as index
        """
        ts = TimeSeries(key=TestAlphaVantageAsync._API_KEY_TEST,
                        output_format='pandas', indexing_type='date')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            if ts.indexing_type == 'date':
                assert isinstance(data.index[0], Timestamp)
            else:
                assert isinstance(data.index[0], str)
        await ts.close()

    @make_async
    async def test_time_series_intraday_date_integer(self):
        """
        Test that api call returns a pandas data frame with an integer as index
        """
        ts = TimeSeries(key=TestAlphaVantageAsync._API_KEY_TEST,
                        output_format='pandas', indexing_type='integer')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey=test&datatype=json"
        path_file = self.get_file_from_url("mock_time_series")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ts.get_intraday(
                "MSFT", interval='1min', outputsize='full')
            assert type(data.index[0]) == int
        await ts.close()

    @make_async
    async def test_technical_indicator_sma_python3(self):
        """
        Test that api call returns a json file as requested
        """
        ti = TechIndicators(key=TestAlphaVantageAsync._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url("mock_technical_indicator")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ti.get_sma("MSFT", interval='15min',
                                       time_period=10, series_type='close')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await ti.close()

    @make_async
    async def test_technical_indicator_sma_pandas(self):
        """
        Test that api call returns a json file as requested
        """
        ti = TechIndicators(
            key=TestAlphaVantageAsync._API_KEY_TEST, output_format='pandas')
        url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=test"
        path_file = self.get_file_from_url("mock_technical_indicator")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await ti.get_sma("MSFT", interval='15min',
                                       time_period=10, series_type='close')
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')
        await ti.close()

    @make_async
    async def test_sector_perfomance_python3(self):
        """
        Test that api call returns a json file as requested
        """
        sp = SectorPerformances(key=TestAlphaVantageAsync._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url("mock_sector")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await sp.get_sector()
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await sp.close()

    @make_async
    async def test_sector_perfomance_pandas(self):
        """
        Test that api call returns a json file as requested
        """
        sp = SectorPerformances(
            key=TestAlphaVantageAsync._API_KEY_TEST, output_format='pandas')
        url = "https://www.alphavantage.co/query?function=SECTOR&apikey=test"
        path_file = self.get_file_from_url("mock_sector")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await sp.get_sector()
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')
        await sp.close()

    @make_async
    async def test_foreign_exchange(self):
        """
        Test that api call returns a json file as requested
        """
        fe = ForeignExchange(key=TestAlphaVantageAsync._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=test"
        path_file = self.get_file_from_url("mock_foreign_exchange")
        with open(path_file) as f, aioresponses() as m:
            m.get(url, payload=json.loads(f.read()))
            data, _ = await fe.get_currency_exchange_rate(
                from_currency='BTC', to_currency='CNY')
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
        await fe.close()
