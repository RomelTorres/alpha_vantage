#!/usr/bin/env python
from alpha_vantage.api_calls.alphavantage import AlphaVantage
from alpha_vantage.api_calls.timeseries import TimesSeries
from alpha_vantage.api_calls.techindicators import TechIndicators
from simplejson import loads, dumps
import unittest
import timeit
import os

class TestAlphaVantage(unittest.TestCase):
    """
        Test data request different implementations
    """
    _API_KEY_TEST = os.environ['API_KEY']
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
            ti = AlphaVantage()
            self.fail(msg='A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    def test_get_intraday_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ts = TimesSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ts.get_intraday,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_daily_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ts = TimesSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ts.get_daily,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_weekly_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ts = TimesSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ts.get_weekly,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_monthly_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ts = TimesSeries(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ts.get_monthly,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sma_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_sma,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)


    def test_get_ema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_wma_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_wma,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_dema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dema_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_tema,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trima_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_trima,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_kama_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_kama,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mama_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_mama,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_t3_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_t3,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macd_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_macd,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_macdext_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_macdext,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stoch_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_stoch,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochf_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_stochf,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_rsi_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_rsi,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_stochrsi_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_stochrsi,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_willr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_willr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adx_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_adx,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adxr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_adxr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_apo_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_apo,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ppo_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ppo,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mom_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_mom,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_bop_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_bop,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_cci_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_cci,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_cmo_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_cmo,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_roc_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_roc,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_rocr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_rocr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_aroon_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_aroon,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_aroonosc_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_aroonosc,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_mfi_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_mfi,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trix_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_trix,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ultsoc_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ultsoc,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_dx_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_dx,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_minus_di_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_minus_di,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_plus_di_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_plus_di,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_minus_dm_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_minus_dm,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_plus_dm_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_plus_dm,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_bbands_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_bbands,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_midpoint_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_midpoint,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_midprice_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_midprice,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_sar_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_sar,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_trange_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_trange,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_atr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_atr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_natr_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_natr,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ad_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ad,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_adosc_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_adosc,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_obv_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_obv,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_trendline_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_trendline,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_sine_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_sine,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_trendmode_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_trendmode,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_dcperiod_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_dcperiod,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_dcphase_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_dcphase,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)

    def test_get_ht_phasor_is_dict(self):
        """Result must be a dictionary containning the json data
        """
        ti = TechIndicators(key=TestAlphaVantage._API_KEY_TEST)
        self._assert_result_is_dict(ti.get_ht_phasor,
        symbol=TestAlphaVantage._API_EQ_NAME_TEST)
