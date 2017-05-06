#!/usr/bin/env python
from alpha_vantage.alphavantage import AlphaVantage
from simplejson import loads, dumps
import unittest
import timeit

class TestAlphaVantage(unittest.TestCase):
    """
        Test data request different implementations
    """
    _API_KEY_TEST = '486U'
    _API_EQ_NAME_TEST = 'MSFT'

    def _assert_result_is_dict(self, func, **args):
        """ Check that the data and meta data object are dictionaries
        """
        stime = timeit.default_timer()
        data, meta_data = func(**args)
        elapsed = timeit.default_timer() - stime
        print('Function {} - took :{}'.format(func.__name__, elapsed))
        self.assertIsInstance(data, dict, 'Result Data must be a dictionary')
        self.assertIsInstance(meta_data, dict, 'Result Meta Data must be a \
        dictionary')

    def test_key_none(self):
        """Raise an error when a key has not been given
        """
        try:
            av = AlphaVantage()
            self.fail(msg='A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    def test_get_intraday_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_intraday,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_daily_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_daily,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_weekly_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_weekly,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_monthly_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_monthly,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sma_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_sma,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)


    def test_get_ema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_ema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_wma_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_wma,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_dema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_tema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trima_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_trima,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_kama_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_kama,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mama_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_mama,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_t3_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_t3,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macd_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_macd,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macdext_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_macdext,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stoch_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_stoch,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochf_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_stochf,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_rsi_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_rsi,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochrsi_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_stochrsi,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_willr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_willr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adx_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(av.get_adx,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)
