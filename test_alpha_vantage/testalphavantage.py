#!/usr/bin/env python
from ..alpha_vantage.alphavantage import AlphaVantage
from ..alpha_vantage.timeseries import TimeSeries
from ..alpha_vantage.techindicators import TechIndicators
from ..alpha_vantage.sectorperformance import SectorPerformances
from ..alpha_vantage.cryptocurrencies import CryptoCurrencies
from nose.tools import assert_true
from pandas import DataFrame as df

import unittest
import timeit
import os
import time


class TestAlphaVantage(unittest.TestCase):
    """
        Test data request different implementations
    """
    _API_KEY_TEST = os.environ['API_KEY']
    _API_EQ_NAME_TEST = 'MSFT'

    def _assert_result_is_format(self, func, output_format='json',  **args):
        """Check that the data and meta data object are dictionaries

        Keyword arguments
        func -- the function to assert its format
        output_format -- the format of the call
        **args -- The parameteres for the call
        """
        stime = timeit.default_timer()
        data, meta_data = func(**args)
        elapsed = timeit.default_timer() - stime
        # TODO: WORKaround to not call the api that often when testing
        time.sleep(0.3)
        print('Function: {} - Format: {} - Took: {}'.format(func.__name__,
                                                            output_format, elapsed))
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

    def test_exchange_supported(self):
        """ Check that the function returns false when asked for an  unsupported
        exchange.
        """
        av = AlphaVantage(key=TestAlphaVantage._API_KEY_TEST)
        assert_true(av.is_exchange_supported('ETR') is not None)
        assert_true(av.is_exchange_supported('Nonsense') is None)

    def test_get_intraday_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ts.get_intraday,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        self._assert_result_is_format(ts.get_intraday, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_daily_is_format(self):
        """Result must be a dictionary containning the json data
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
        """Result must be a dictionary containning the json data
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

    def test_get_weekly_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ts.get_weekly,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        self._assert_result_is_format(ts.get_weekly, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_monthly_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ts.get_monthly,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ts = TimeSeries(key=TestAlphaVantage._API_KEY_TEST,
                        output_format='pandas')
        self._assert_result_is_format(ts.get_monthly, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sma_is_format(self):
        """Result must be a dictionary containning the json data
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
        """Result must be a dictionary containning the json data
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

    def test_get_wma_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_wma,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_wma, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dema_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_dema,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_dema, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trima_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_trima,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_trima, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_kama_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_kama,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_kama, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mama_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_mama,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_mama, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_t3_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_t3,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_t3, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macd_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_macd,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_macd, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macdext_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_macdext,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_macdext, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stoch_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_stoch,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_stoch, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochf_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_stochf,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_stochf, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_rsi_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_rsi,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_rsi, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochrsi_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_stochrsi,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_stochrsi, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_willr_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_willr,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_willr, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adx_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_adx,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_adx, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adxr_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_adxr,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_adxr, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_apo_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_apo,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_apo, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ppo_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ppo,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ppo, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mom_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_mom,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_mom, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_bop_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_bop,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_bop, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_cci_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_cci,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_cci, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_cmo_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_cmo,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_cmo, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_roc_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_roc,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_roc, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_rocr_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_rocr,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_rocr, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_aroon_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_aroon,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_aroon, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_aroonosc_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_aroonosc,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_aroonosc, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mfi_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_mfi,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_mfi, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trix_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_trix,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_trix, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ultsoc_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ultsoc,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ultsoc, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dx_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_dx,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_dx, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_minus_di_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_minus_di,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_minus_di, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_plus_di_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_plus_di,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_plus_di, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_minus_dm_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_minus_dm,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_minus_dm, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_plus_dm_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_plus_dm,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_plus_dm, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_bbands_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_bbands,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_bbands, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_midpoint_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_midpoint,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_midpoint, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_midprice_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_midprice,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_midprice, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sar_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_sar,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_sar, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trange_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_trange,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_trange, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_atr_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_atr,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_atr, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_natr_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_natr,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_natr, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ad_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ad,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ad, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adosc_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_adosc,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_adosc, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_obv_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_obv,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_obv, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_trendline_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_trendline,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_trendline, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_sine_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_sine,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_sine, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_trendmode_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_trendmode,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_trendmode, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_dcperiod_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_dcperiod,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_dcperiod, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_dcphase_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_dcphase,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_dcphase, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_phasor_is_format(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(ti.get_ht_phasor,
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)
        # Test panda as output
        ti = TechIndicators(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(ti.get_ht_phasor, output_format='pandas',
                                      symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sector(self):
        """Result must be a dictionary containning the json data
        """
        # Test dictionary as output
        sp = SectorPerformances(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(sp.get_sector)
        # Test panda as output
        sp = SectorPerformances(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(sp.get_sector, output_format='pandas')

    def test_get_currency_exchange_rate(self):
        """Test that we get a dictionary containning json data
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_currency_exchange_rate,
                                      output_format='json',
                                      from_currency='BTC',
                                      to_currency='USD')

    def test_get_digital_currency_intraday(self):
        """Test that we get a dictionary containning json data
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_digital_currency_intraday,
                                      output_format='json',
                                      symbol='BTC',
                                      market='CNY')
        # Test panda as output
        cc = CryptoCurrencies(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(cc.get_digital_currency_intraday,
                                      output_format='pandas',
                                      symbol='BTC',
                                      market='CNY')

    def test_get_digital_currency_daily(self):
        """Test that we get a dictionary containning json data
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_digital_currency_daily,
                                      output_format='json',
                                      symbol='BTC',
                                      market='CNY')
        # Test panda as output
        cc = CryptoCurrencies(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(cc.get_digital_currency_daily,
                                      output_format='pandas',
                                      symbol='BTC',
                                      market='CNY')

    def test_get_digital_currency_weekly(self):
        """Test that we get a dictionary containning json data
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

    def test_get_digital_currency_monthly(self):
        """Test that we get a dictionary containning json data
        """
        cc = CryptoCurrencies(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_format(cc.get_digital_currency_monthly,
                                      output_format='json',
                                      symbol='BTC',
                                      market='CNY')
        # Test panda as output
        cc = CryptoCurrencies(
            key=TestAlphaVantage._API_KEY_TEST, output_format='pandas')
        self._assert_result_is_format(cc.get_digital_currency_monthly,
                                      output_format='pandas',
                                      symbol='BTC',
                                      market='CNY')
