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
