#! /usr/bin/env python
import unittest

from pandas import DataFrame as df

import requests_mock

from ..alpha_vantage.commodities import Commodities


class TestCommodities(unittest.TestCase):

    _API_KEY_TEST = "test"

    @requests_mock.Mocker()
    def test_silver_spot(self, mock_request):
        """Test that silver spot prices are requested correctly"""
        commodities = Commodities(key=self._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=SILVER&apikey=test&datatype=json"
        mock_request.get(url, json={
            "nominal": "XAGUSD",
            "timestamp": "2026-06-21 16:52:43",
            "price": "64.840366422"
        })
        data, meta_data = commodities.get_silver_spot()
        assert isinstance(data, dict)
        assert data['nominal'] == 'XAGUSD'
        assert meta_data is None

    @requests_mock.Mocker()
    def test_gold_spot_with_xau_symbol(self, mock_request):
        """Test that gold spot prices support XAU as documented"""
        commodities = Commodities(key=self._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=GOLD_SILVER_SPOT&symbol=XAU&apikey=test&datatype=json"
        mock_request.get(url, json={
            "nominal": "XAUUSD",
            "timestamp": "2026-06-21 16:52:43",
            "price": "4155.5747450763"
        })
        data, meta_data = commodities.get_gold_spot(symbol='XAU')
        assert isinstance(data, dict)
        assert data['nominal'] == 'XAUUSD'
        assert meta_data is None

    @requests_mock.Mocker()
    def test_silver_history(self, mock_request):
        """Test that silver history prices are requested correctly"""
        commodities = Commodities(key=self._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&interval=daily&symbol=SILVER&apikey=test&datatype=json"
        mock_request.get(url, json={
            "nominal": "XAGUSD",
            "data": [
                {"date": "2026-06-20", "price": "64.8413998488"},
                {"date": "2026-06-19", "price": "65.3517075323"}
            ]
        })
        data, meta_data = commodities.get_silver(interval='daily')
        assert isinstance(data, df)
        assert list(data.columns) == ['date', 'price']
        assert meta_data == 'XAGUSD'

    @requests_mock.Mocker()
    def test_gold_history_with_xau_symbol(self, mock_request):
        """Test that gold history prices support XAU as documented"""
        commodities = Commodities(key=self._API_KEY_TEST)
        url = "https://www.alphavantage.co/query?function=GOLD_SILVER_HISTORY&interval=weekly&symbol=XAU&apikey=test&datatype=json"
        mock_request.get(url, json={
            "nominal": "XAUUSD",
            "data": [
                {"date": "2026-06-20", "price": "4155.5747450763"},
                {"date": "2026-06-13", "price": "4101.141"}
            ]
        })
        data, meta_data = commodities.get_gold(interval='weekly', symbol='XAU')
        assert isinstance(data, df)
        assert list(data.columns) == ['date', 'price']
        assert meta_data == 'XAUUSD'
