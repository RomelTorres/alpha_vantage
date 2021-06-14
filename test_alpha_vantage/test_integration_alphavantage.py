#!/usr/bin/env python
from ..alpha_vantage.alphavantage import AlphaVantage
from ..alpha_vantage.timeseries import TimeSeries
from ..alpha_vantage.techindicators import TechIndicators
from ..alpha_vantage.cryptocurrencies import CryptoCurrencies
from ..alpha_vantage.foreignexchange import ForeignExchange

from pandas import DataFrame as df

import os
import unittest
import timeit
import time


class TestAlphaVantage(unittest.TestCase):
    """
        Test data request different implementations
    """
    _API_KEY_TEST = os.environ['API_KEY']
    _API_EQ_NAME_TEST = 'MSFT'
    _RAPIDAPI_KEY_TEST = os.getenv("RAPIDAPI_KEY")

    def setUp(self):
        """
        Wait some time before running each call again.
        """
        time.sleep(1)

    def _assert_result_is_format(self, func, output_format='json', **args):
        """Check that the data and meta data object are dictionaries

        Keyword arguments
        func -- the function to assert its format
        output_format -- the format of the call
        **args -- The parameters for the call
        """
        stime = timeit.default_timer()
        data, meta_data = func(**args)
        elapsed = timeit.default_timer() - stime
        print('Function: {} - Format: {} - Took: {}'.format(func.__name__,
                                                            output_format,
                                                            elapsed))
        if output_format == 'json':
            self.assertIsInstance(
                data, dict, 'Result Data must be a dictionary')
            if meta_data is not None:
                self.assertIsInstance(meta_data, dict, 'Result Meta Data must be a \
                dictionary')
        elif output_format == 'pandas':
            self.assertIsInstance(
                data, df, 'Result Data must be a pandas data frame')
            if meta_data is not None:
                self.assertIsInstance(meta_data, dict, 'Result Meta Data must be a \
                dictionary')

    def test_key_none(self):
        """Raise an error when a key has not been given
        """
        try:
            AlphaVantage()
            self.fail(msg='A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    def test_rapidapi_key_with_get_daily(self):
        """RapidAPI calls must return the same data as non-rapidapi calls
        """
        # Test rapidAPI calls are the same as regular ones
        ts_rapidapi = TimeSeries(
            key=TestAlphaVantage._RAPIDAPI_KEY_TEST, rapidapi=True)
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        rapidapi_data, _ = ts_rapidapi.get_daily(
            symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        data, _ = ts.get_daily(
            symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        self.assertTrue(rapidapi_data == data)

    def test_get_daily_is_format(self):
        """Result must be a dictionary containing the json data
        """
        # Test dictionary as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ts.get_daily,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        self._assert_result_is_format(ts.get_daily, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_daily_adjusted_is_format(self):
        """Result must be a dictionary containing the json data
        """
        # Test dictionary as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ts.get_daily_adjusted,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        self._assert_result_is_format(ts.get_daily_adjusted, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sma_is_format(self):
        """Result must be a dictionary containing the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_sma,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_sma, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ema_is_format(self):
        """Result must be a dictionary containing the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ema,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ema, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_currency_exchange_rate(self):
        """Test that we get a dictionary containing json data
        """
        cc = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_currency_exchange_rate,
                                      output_format='json',
                                      from_currency='USD',
                                      to_currency='BTC')

    def test_get_currency_exchange_intraday_json(self):
        """Test that we get a dictionary containing json data
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(fe.get_currency_exchange_intraday,
                                      output_format='json',
                                      from_symbol='EUR',
                                      to_symbol='USD',
                                      interval='1min')

    def test_get_currency_exchange_intraday_pandas(self):
        """Test that we get a dictionary containing pandas data
        """
        fe = ForeignExchange(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(fe.get_currency_exchange_intraday,
                                      output_format='pandas',
                                      from_symbol='USD',
                                      to_symbol='JPY',
                                      interval='5min')

    def test_get_currency_exchange_daily_json(self):
        """Test that we get a dictionary containing json data
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(fe.get_currency_exchange_daily,
                                      output_format='json',
                                      from_symbol='EUR',
                                      to_symbol='USD')

    def test_get_currency_exchange_daily_pandas(self):
        """Test that we get a dictionary containing pandas data
        """
        fe = ForeignExchange(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(fe.get_currency_exchange_daily,
                                      output_format='pandas',
                                      from_symbol='USD',
                                      to_symbol='JPY')

    def test_get_currency_exchange_weekly_json(self):
        """Test that we get a dictionary containing json data
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(fe.get_currency_exchange_weekly,
                                      output_format='json',
                                      from_symbol='EUR',
                                      to_symbol='USD',
                                      outputsize='full')

    def test_get_currency_exchange_weekly_pandas(self):
        """Test that we get a dictionary containing pandas data
        """
        fe = ForeignExchange(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(fe.get_currency_exchange_weekly,
                                      output_format='pandas',
                                      from_symbol='USD',
                                      to_symbol='JPY')

    def test_get_currency_exchange_monthly_json(self):
        """Test that we get a dictionary containing json data
        """
        fe = ForeignExchange(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(fe.get_currency_exchange_monthly,
                                      output_format='json',
                                      from_symbol='EUR',
                                      to_symbol='USD')

    def test_get_currency_exchange_monthly_pandas(self):
        """Test that we get a dictionary containing pandas data
        """
        fe = ForeignExchange(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(fe.get_currency_exchange_monthly,
                                      output_format='pandas',
                                      from_symbol='USD',
                                      to_symbol='JPY',
                                      outputsize='full')

    def test_get_digital_currency_weekly(self):
        """Test that we get a dictionary containing json data
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_digital_currency_weekly,
                                      output_format='json',
                                      symbol='BTC',
                                      market='CNY')
        # Test panda as output
        cc = CryptoCurrencies(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(cc.get_digital_currency_weekly,
                                      output_format='pandas',
                                      symbol='BTC',
                                      market='CNY')
