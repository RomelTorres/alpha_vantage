from .alphavantage import AlphaVantage as av


class TechIndicators(av):
    """This class implements all the technical indicator api calls
    """

    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments
        """
        super(TechIndicators, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not comatible with the TechIndicators class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_sma(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return simple moving average time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "SMA"
        return _FUNCTION_KEY, 'Technical Analysis: SMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ema(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return exponential moving average time series in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "EMA"
        return _FUNCTION_KEY, 'Technical Analysis: EMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_wma(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return weighted moving average time series in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "WMA"
        return _FUNCTION_KEY, 'Technical Analysis: WMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_dema(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return double exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "DEMA"
        return _FUNCTION_KEY, 'Technical Analysis: DEMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_tema(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return triple exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "TEMA"
        return _FUNCTION_KEY, 'Technical Analysis: TEMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trima(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return triangular moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "TRIMA"
        return _FUNCTION_KEY, 'Technical Analysis: TRIMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_kama(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return Kaufman adaptative moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "KAMA"
        return _FUNCTION_KEY, 'Technical Analysis: KAMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mama(self, symbol, interval='daily', series_type='close', month='',
                 fastlimit=None, slowlimit=None):
        """ Return MESA adaptative moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastlimit:  Positive floats for the fast limit are accepted
                (default=None)
            slowlimit:  Positive floats for the slow limit are accepted
                (default=None)
        """
        _FUNCTION_KEY = "MAMA"
        return _FUNCTION_KEY, 'Technical Analysis: MAMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_vwap(self, symbol, interval='1min',  month=''):
        """ Returns the volume weighted average price (VWAP) for intraday time series.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min' 
                (default 5min)
        """
        _FUNCTION_KEY = "VWAP"
        return _FUNCTION_KEY, 'Technical Analysis: VWAP', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_t3(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return triple exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "T3"
        return _FUNCTION_KEY, 'Technical Analysis: T3', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_macd(self, symbol, interval='daily', series_type='close',
                 fastperiod=None, slowperiod=None, signalperiod=None, month=''):
        """ Return the moving average convergence/divergence time series in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily'
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastperiod:  Positive integers are accepted (default=None)
            slowperiod:  Positive integers are accepted (default=None)
            signalperiod:  Positive integers are accepted (default=None)
        """
        _FUNCTION_KEY = "MACD"
        return _FUNCTION_KEY, 'Technical Analysis: MACD', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_macdext(self, symbol, interval='daily', series_type='close',
                    fastperiod=None, slowperiod=None, signalperiod=None, fastmatype=None,
                    slowmatype=None, signalmatype=None, month=''):
        """ Return the moving average convergence/divergence time series in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastperiod:  Positive integers are accepted (default=None)
            slowperiod:  Positive integers are accepted (default=None)
            signalperiod:  Positive integers are accepted (default=None)
            fastmatype:  Moving average type for the faster moving average.
                By default, fastmatype=0. Integers 0 - 8 are accepted
                (check  down the mappings) or the string containing the math type can
                also be used.
            slowmatype:  Moving average type for the slower moving average.
                By default, slowmatype=0. Integers 0 - 8 are accepted
                (check down the mappings) or the string containing the math type can
                also be used.
            signalmatype:  Moving average type for the signal moving average.
                By default, signalmatype=0. Integers 0 - 8 are accepted
                (check down the mappings) or the string containing the math type can
                also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "MACDEXT"
        return _FUNCTION_KEY, 'Technical Analysis: MACDEXT', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stoch(self, symbol, interval='daily', fastkperiod=None,
                  slowkperiod=None, slowdperiod=None, slowkmatype=None, slowdmatype=None, month=''):
        """ Return the stochatic oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            fastkperiod:  The time period of the fastk moving average. Positive
                integers are accepted (default=None)
            slowkperiod:  The time period of the slowk moving average. Positive
                integers are accepted (default=None)
            slowdperiod: The time period of the slowd moving average. Positive
                integers are accepted (default=None)
            slowkmatype:  Moving average type for the slowk moving average.
                By default, fastmatype=0. Integers 0 - 8 are accepted
                (check  down the mappings) or the string containing the math type can
                also be used.
            slowdmatype:  Moving average type for the slowd moving average.
                By default, slowmatype=0. Integers 0 - 8 are accepted
                (check down the mappings) or the string containing the math type can
                also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)

            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "STOCH"
        return _FUNCTION_KEY, 'Technical Analysis: STOCH', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stochf(self, symbol, interval='daily', fastkperiod=None,
                   fastdperiod=None, fastdmatype=None, month=''):
        """ Return the stochatic oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            fastkperiod:  The time period of the fastk moving average. Positive
                integers are accepted (default=None)
            fastdperiod:  The time period of the fastd moving average. Positive
                integers are accepted (default=None)
            fastdmatype:  Moving average type for the fastdmatype moving average.
                By default, fastmatype=0. Integers 0 - 8 are accepted
                (check  down the mappings) or the string containing the math type can
                also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "STOCHF"
        return _FUNCTION_KEY, 'Technical Analysis: STOCHF', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_rsi(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the relative strength index time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "RSI"
        return _FUNCTION_KEY, 'Technical Analysis: RSI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stochrsi(self, symbol, interval='daily', time_period=20,
                     series_type='close', fastkperiod=None, fastdperiod=None, fastdmatype=None, month=''):
        """ Return the stochatic relative strength index in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastkperiod:  The time period of the fastk moving average. Positive
                integers are accepted (default=None)
            fastdperiod:  The time period of the fastd moving average. Positive
                integers are accepted (default=None)
            fastdmatype:  Moving average type for the fastdmatype moving average.
                By default, fastmatype=0. Integers 0 - 8 are accepted
                (check  down the mappings) or the string containing the math type can
                also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "STOCHRSI"
        return _FUNCTION_KEY, 'Technical Analysis: STOCHRSI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_willr(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the Williams' %R (WILLR) values in two json objects as data
        and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "WILLR"
        return _FUNCTION_KEY, 'Technical Analysis: WILLR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adx(self, symbol, interval='daily', time_period=20, month=''):
        """ Return  the average directional movement index values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ADX"
        return _FUNCTION_KEY, 'Technical Analysis: ADX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adxr(self, symbol, interval='daily', time_period=20, month=''):
        """ Return  the average directional movement index  rating in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ADXR"
        return _FUNCTION_KEY, 'Technical Analysis: ADXR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_apo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None, month=''):
        """ Return the absolute price oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default '60min)'
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastperiod:  Positive integers are accepted (default=None)
            slowperiod:  Positive integers are accepted (default=None)
            matype    :  Moving average type. By default, fastmatype=0.
                Integers 0 - 8 are accepted (check  down the mappings) or the string
                containing the math type can also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "APO"
        return _FUNCTION_KEY, 'Technical Analysis: APO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ppo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None, month=''):
        """ Return the percentage price oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily'
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            fastperiod:  Positive integers are accepted (default=None)
            slowperiod:  Positive integers are accepted (default=None)
            matype    :  Moving average type. By default, fastmatype=0.
                Integers 0 - 8 are accepted (check  down the mappings) or the string
                containing the math type can also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "PPO"
        return _FUNCTION_KEY, 'Technical Analysis: PPO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mom(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the momentum values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MOM"
        return _FUNCTION_KEY, 'Technical Analysis: MOM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_bop(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the balance of power values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
        month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "BOP"
        return _FUNCTION_KEY, 'Technical Analysis: BOP', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_cci(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the commodity channel index values  in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
        month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "CCI"
        return _FUNCTION_KEY, 'Technical Analysis: CCI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_cmo(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the Chande momentum oscillator in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "CMO"
        return _FUNCTION_KEY, 'Technical Analysis: CMO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_roc(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the rate of change values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ROC"
        return _FUNCTION_KEY, 'Technical Analysis: ROC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_rocr(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the rate of change ratio values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ROCR"
        return _FUNCTION_KEY, 'Technical Analysis: ROCR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_aroon(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the aroon values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "AROON"
        return _FUNCTION_KEY, 'Technical Analysis: AROON', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_aroonosc(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the aroon oscillator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "AROONOSC"
        return _FUNCTION_KEY, 'Technical Analysis: AROONOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mfi(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the money flow index values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MFI"
        return _FUNCTION_KEY, 'Technical Analysis: MFI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trix(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the1-day rate of change of a triple smooth exponential
        moving average in two json objects as data and meta_data.
        It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "TRIX"
        return _FUNCTION_KEY, 'Technical Analysis: TRIX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ultosc(self, symbol, interval='daily', timeperiod1=None,
                   timeperiod2=None, timeperiod3=None, month=''):
        """ Return the ultimate oscillaror values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            timeperiod1:  The first time period indicator. Positive integers are
                accepted. By default, timeperiod1=7
            timeperiod2:  The first time period indicator. Positive integers are
                accepted. By default, timeperiod2=14
            timeperiod3:  The first time period indicator. Positive integers are
                accepted. By default, timeperiod3=28
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ULTOSC"
        return _FUNCTION_KEY, 'Technical Analysis: ULTOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_dx(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the directional movement index values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "DX"
        return _FUNCTION_KEY, 'Technical Analysis: DX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_minus_di(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the minus directional indicator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MINUS_DI"
        return _FUNCTION_KEY, 'Technical Analysis: MINUS_DI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_plus_di(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the plus directional indicator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "PLUS_DI"
        return _FUNCTION_KEY, 'Technical Analysis: PLUS_DI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_minus_dm(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the minus directional movement values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MINUS_DM"
        return _FUNCTION_KEY, 'Technical Analysis: MINUS_DM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_plus_dm(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the plus directional movement values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "PLUS_DM"
        return _FUNCTION_KEY, 'Technical Analysis: PLUS_DM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_bbands(self, symbol, interval='daily', time_period=20,  series_type='close',
                   nbdevup=None, nbdevdn=None, matype=None, month=''):
        """ Return the bollinger bands values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  Number of data points used to calculate each BBANDS value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
                (default=20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            nbdevup:  The standard deviation multiplier of the upper band. Positive
                integers are accepted as default (default=2)
            nbdevdn:  The standard deviation multiplier of the lower band. Positive
                integers are accepted as default (default=2)
            matype :  Moving average type. By default, matype=0.
                Integers 0 - 8 are accepted (check  down the mappings) or the string
                containing the math type can also be used.

                * 0 = Simple Moving Average (SMA),
                * 1 = Exponential Moving Average (EMA),
                * 2 = Weighted Moving Average (WMA),
                * 3 = Double Exponential Moving Average (DEMA),
                * 4 = Triple Exponential Moving Average (TEMA),
                * 5 = Triangular Moving Average (TRIMA),
                * 6 = T3 Moving Average,
                * 7 = Kaufman Adaptive Moving Average (KAMA),
                * 8 = MESA Adaptive Moving Average (MAMA)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "BBANDS"
        return _FUNCTION_KEY, 'Technical Analysis: BBANDS', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_midpoint(self, symbol, interval='daily', time_period=20, series_type='close', month=''):
        """ Return the midpoint values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MIDPOINT"
        return _FUNCTION_KEY, 'Technical Analysis: MIDPOINT', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_midprice(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the midprice values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "MIDPRICE"
        return _FUNCTION_KEY, 'Technical Analysis: MIDPRICE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_sar(self, symbol, interval='daily', acceleration=None, maximum=None, month=''):
        """ Return the midprice values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            acceleration:  The acceleration factor. Positive floats are accepted (
                default 0.01)
            maximum:  The acceleration factor maximum value. Positive floats
                are accepted (default 0.20 )
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "SAR"
        return _FUNCTION_KEY, 'Technical Analysis: SAR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trange(self, symbol, interval='daily', month=''):
        """ Return the true range values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "TRANGE"
        return _FUNCTION_KEY, 'Technical Analysis: TRANGE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_atr(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the average true range values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ATR"
        return _FUNCTION_KEY, 'Technical Analysis: ATR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_natr(self, symbol, interval='daily', time_period=20, month=''):
        """ Return the normalized average true range values in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            time_period:  How many data points to average (default 20)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "NATR"
        return _FUNCTION_KEY, 'Technical Analysis: NATR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ad(self, symbol, interval='daily', month=''):
        """ Return the Chaikin A/D line values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "AD"
        return _FUNCTION_KEY, 'Technical Analysis: Chaikin A/D', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adosc(self, symbol, interval='daily', fastperiod=None,
                  slowperiod=None, month=''):
        """ Return the Chaikin A/D oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily'
            fastperiod:  Positive integers are accepted (default=None)
            slowperiod:  Positive integers are accepted (default=None)
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "ADOSC"
        return _FUNCTION_KEY, 'Technical Analysis: ADOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_obv(self, symbol, interval='daily', month=''):
        """ Return the on balance volume values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "OBV"
        return _FUNCTION_KEY, 'Technical Analysis: OBV', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_trendline(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, instantaneous trendline values in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_TRENDLINE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_TRENDLINE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_sine(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, sine wave values in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
            are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_SINE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_SINE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_trendmode(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, trend vs cycle mode in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_TRENDMODE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_TRENDMODE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_dcperiod(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, dominant cycle period in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_DCPERIOD"
        return _FUNCTION_KEY, 'Technical Analysis: HT_DCPERIOD', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_dcphase(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, dominant cycle phase in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_DCPHASE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_DCPHASE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_phasor(self, symbol, interval='daily', series_type='close', month=''):
        """ Return the Hilbert transform, phasor components in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', 'monthly' (default 'daily')
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "HT_PHASOR"
        return _FUNCTION_KEY, 'Technical Analysis: HT_PHASOR', 'Meta Data'
