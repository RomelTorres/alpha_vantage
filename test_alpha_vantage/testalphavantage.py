#!/usr/bin/env python
from alpha_vantage.alphavantage import AlphaVantage
import unittest
from simplejson import loads, dumps

class TestAlphaVantage(unittest.TestCase):
    """
        Test data request different implementations
    """
    _API_KEY_TEST = '486U'
    _API_EQ_NAME_TEST = 'MSFT'

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
        data, meta_data = av.get_intraday(TestAlphaVantage._API_EQ_NAME_TEST)
        self.assertIsInstance(data, dict, 'Result Data must be a dictionary')
        self.assertIsInstance(meta_data, dict, 'Result Meta Data must be a \
        dictionary')

    def test_intraday_error(self):
        """A Value error must be raised when a parameter is wrong
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        try:
            data, meta_data = av.get_intraday('nonsense')
            self.fail(msg='An error should be raised when using an non \
            existent hey')
        except ValueError:
            self.assertTrue(True)

    def test_get_intraday_integrity(self):
        """ Test that the data returned by the api is more or less
        what we expected
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        data, meta_data = av.get_intraday(TestAlphaVantage._API_EQ_NAME_TEST)
        self.assertTrue(len(data) == 100, "The dictionary size for the default \
        outputsize ('compact') has to be 100")
        data, meta_data = av.get_intraday(TestAlphaVantage._API_EQ_NAME_TEST,
        outputsize='full')
        self.assertTrue(len(data) > 100, 'The dictionary size for the default \
        outputsize has to be 100')

    def test_get_daily_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        data, meta_data = av.get_daily(TestAlphaVantage._API_EQ_NAME_TEST)
        self.assertIsInstance(data, dict, 'Result Data must be a dictionary')
        self.assertIsInstance(meta_data, dict, 'Result Meta Data must be a \
        dictionary')

    def test_daily_error(self):
        """A Value error must be raised when a parameter is wrong
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        try:
            data, meta_data = av.get_daily('nonsense')
            self.fail(msg='An error should be raised when using an non \
            existent hey')
        except ValueError:
            self.assertTrue(True)

    def test_get_daily_integrity(self):
        """ Test that the data returned by the api is more or less
        what we expected
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        data, meta_data = av.get_daily(TestAlphaVantage._API_EQ_NAME_TEST)
        self.assertTrue(len(data) == 100, "The dictionary size for the default \
        outputsize ('compact') has to be 100")
        data, meta_data = av.get_daily(TestAlphaVantage._API_EQ_NAME_TEST,
        outputsize='full')
        self.assertTrue(len(data) > 100, 'The dictionary size for the default \
        outputsize has to be 100')
