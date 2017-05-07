try:
    # Python 3 import
    from urllib.request import urlopen
except ImportError:
    # Python 2.* import
    from urllib2 import urlopen

from simplejson import loads




class AlphaVantage:
    """
        This class is in charge of creating a python interface between the Alpha
        Vantage restful API and your python application
    """
    _ALPHA_VANTAGE_API_URL = "http://www.alphavantage.co/query?"
    _ALPHA_VANTAGE_MATH_MAP = ['SMA','EMA','WMA','DEMA','TEMA', 'TRIMA','T3',
    'KAMA','MAMA']
    def __init__(self, key=None, retries=0):
        if key is None:
            raise ValueError('Get a free key from the alphavantage website')
        self.key = key
        self.retries = retries

    def _retry(func):
        """ Decorator for retrying api calls (in case of errors from the api
        side in bringing the data)

        Keyword arguments:
        func -- The function to be retried
        """
        def _retry_wrapper(self, *args, **kwargs):
            for retry in range(self.retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except ValueError as err:
                    pass
            raise ValueError(err)
        return _retry_wrapper

    @_retry
    def _handle_api_call(self, url, data_key, meta_data_key="Meta Data"):
        """ Handle the return call from the  api and return a data and meta_data
        object. It raises a ValueError on problems

        Keyword arguments:
        url -- The url of the service
        data_key -- The key for getting the data from the jso object
        meta_data_key -- The key for getting the meta data information out of
        the json object
        """
        json_response = self._data_request(url)
        if 'Error Message' in json_response or not json_response:
            if json_response:
                raise ValueError('ERROR getting data form api',
                             json_response['Error Message'])
            else:
                raise ValueError('Error getting data from api, no return'\
                 ' message from the api url (possibly wrong symbol/param)')
        data = json_response[data_key]
        meta_data = json_response[meta_data_key]
        return data, meta_data

    def _data_request(self, url):
        """ Request data from the given url and return it as a json
        object. It raises URLError

        Keyword arguments:
        url -- The url of the service
        """
        response = urlopen(url)
        url_response = response.read()
        json_response = loads(url_response)
        return json_response

    def get_intraday(self, symbol, interval='15min', outputsize='compact'):
        """ Return intraday time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min'
        (default '15min')
        outputsize -- The size of the call, supported values are
        'compact' and 'full; the first returns the last 100 points in the
        data series, and 'full' returns the full-length intraday times
        series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = "TIME_SERIES_INTRADAY"
        url = "{}function={}&symbol={}&interval={}&outputsize={}&apikey={}\
        ".format(AlphaVantage._ALPHA_VANTAGE_API_URL, _FUNCTION_KEY,  symbol,
                 interval, outputsize, self.key)
        return self._handle_api_call(url, 'Time Series ({})'.format(interval),
        'Meta Data')

    def get_daily(self, symbol, outputsize='compact'):
        """ Return daily time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        outputsize -- The size of the call, supported values are
        'compact' and 'full; the first returns the last 100 points in the
        data series, and 'full' returns the full-length intraday times
        series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = "TIME_SERIES_DAILY"
        url = "{}function={}&symbol={}&outputsize={}&apikey={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL, _FUNCTION_KEY,  symbol, outputsize,
        self.key)
        return self._handle_api_call(url, 'Time Series (Daily)', 'Meta Data')


    def get_weekly(self, symbol):
        """ Return weekly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        url = "{}function={}&symbol={}&apikey={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL, _FUNCTION_KEY, symbol, self.key)
        return self._handle_api_call(url, 'Weekly Time Series', 'Meta Data')

    def get_monthly(self, symbol):
        """ Return monthly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        url = "{}function={}&symbol={}&apikey={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL, _FUNCTION_KEY, symbol, self.key)
        return self._handle_api_call(url, 'Monthly Time Series', 'Meta Data')

    def get_sma(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return simple moving average time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "SMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: SMA','Meta Data')

    def get_ema(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return exponential moving average time series in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "EMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: EMA','Meta Data')

    def get_wma(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return weighted moving average time series in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "WMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: WMA','Meta Data')

    def get_dema(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return double exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "DEMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: DEMA','Meta Data')

    def get_tema(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return triple exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "TEMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: TEMA','Meta Data')

    def get_trima(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return triangular moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "TRIMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: TRIMA','Meta Data')

    def get_kama(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return Kaufman adaptative moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "KAMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: KAMA','Meta Data')

    def get_mama(self, symbol, interval='60min', time_period=20, series_type='close',
    fastlimit=None, slowlimit=None):
        """ Return MESA adaptative moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastlimit -- Positive floats for the fast limit are accepted
        (default=None)
        slowlimit -- Positive floats for the slow limit are accepted
        (default=None)
        """
        _FUNCTION_KEY = "MAMA"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type)
        if fastlimit:
            url="{}&fastlimit={}".format(url,fastlimit)
        if slowlimit:
            url="{}&slowlimit={}".format(url, slowlimit)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: MAMA','Meta Data')

    def get_t3(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return triple exponential moving average time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "T3"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: T3','Meta Data')

    def get_macd(self, symbol, interval='60min', series_type='close',
    fastperiod=None, slowperiod=None, signalperiod=None):
        """ Return the moving average convergence/divergence time series in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min'
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastperiod -- Positive integers are accepted (default=None)
        slowperiod -- Positive integers are accepted (default=None)
        signalperiod -- Positive integers are accepted (default=None)
        """
        _FUNCTION_KEY = "MACD"
        url = "{}function={}&symbol={}&interval={}&series_type={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval,
        series_type)
        if fastperiod:
            url="{}&fastperiod={}".format(url,fastperiod)
        if slowperiod:
            url="{}&slowperiod={}".format(url, slowperiod)
        if signalperiod:
            url="{}&signalperiod={}".format(url, signalperiod)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: MACD','Meta Data')

    def get_macdext(self, symbol, interval='60min', series_type='close',
    fastperiod=None, slowperiod=None, signalperiod=None, fastmatype=None,
    slowmatype=None, signalmatype=None):
        """ Return the moving average convergence/divergence time series in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastperiod -- Positive integers are accepted (default=None)
        slowperiod -- Positive integers are accepted (default=None)
        signalperiod -- Positive integers are accepted (default=None)
        fastmatype -- Moving average type for the faster moving average.
        By default, fastmatype=0. Integers 0 - 8 are accepted
        (check  down the mappings) or the string containing the math type can
        also be used.
        slowmatype -- Moving average type for the slower moving average.
        By default, slowmatype=0. Integers 0 - 8 are accepted
        (check down the mappings) or the string containing the math type can
        also be used.
        signalmatype -- Moving average type for the signal moving average.
        By default, signalmatype=0. Integers 0 - 8 are accepted
        (check down the mappings) or the string containing the math type can
        also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "MACDEXT"
        url = "{}function={}&symbol={}&interval={}&series_type={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval,
        series_type)
        if fastperiod:
            url="{}&fastperiod={}".format(url,fastperiod)
        if slowperiod:
            url="{}&slowperiod={}".format(url, slowperiod)
        if signalperiod:
            url="{}&signalperiod={}".format(url, signalperiod)
        if fastmatype:
            # Check if it is an integer or a string
            try:
                value = int(fastmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(fastmatype)
            url="{}&fastmatype={}".format(url, value)
        if slowmatype:
            # Check if it is an integer or a string
            try:
                value = int(slowmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(slowmatype)
            url="{}&slowmatype={}".format(url, value)
        if signalmatype:
            # Check if it is an integer or a string
            try:
                value = int(signalmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(signalmatype)
            url="{}&signalmatype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: MACDEXT',
        'Meta Data')

    def get_stoch(self, symbol, interval='60min', fastkperiod=None,
    slowkperiod=None, slowdperiod=None, slowkmatype=None, slowdmatype=None):
        """ Return the stochatic oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        fastkperiod -- The time period of the fastk moving average. Positive
        integers are accepted (default=None)
        slowkperiod -- The time period of the slowk moving average. Positive
        integers are accepted (default=None)
        slowdperiod --The time period of the slowd moving average. Positive
        integers are accepted (default=None)
        slowkmatype -- Moving average type for the slowk moving average.
        By default, fastmatype=0. Integers 0 - 8 are accepted
        (check  down the mappings) or the string containing the math type can
        also be used.
        slowdmatype -- Moving average type for the slowd moving average.
        By default, slowmatype=0. Integers 0 - 8 are accepted
        (check down the mappings) or the string containing the math type can
        also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "STOCH"
        url = "{}function={}&symbol={}&interval={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval)
        if fastkperiod:
            url="{}&fastkperiod={}".format(url,fastkperiod)
        if slowkperiod:
            url="{}&slowkperiod={}".format(url, slowkperiod)
        if slowdperiod:
            url="{}&slowdperiod={}".format(url, slowdperiod)
        if slowkmatype:
            # Check if it is an integer or a string
            try:
                value = int(slowkmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(slowkmatype)
            url="{}&slowkmatype={}".format(url, value)
        if slowdmatype:
            # Check if it is an integer or a string
            try:
                value = int(slowdmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(slowdmatype)
            url="{}&slowdmatype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: STOCH',
        'Meta Data')

    def get_stochf(self, symbol, interval='60min', fastkperiod=None,
    fastdperiod=None, fastdmatype=None):
        """ Return the stochatic oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        fastkperiod -- The time period of the fastk moving average. Positive
        integers are accepted (default=None)
        fastdperiod -- The time period of the fastd moving average. Positive
        integers are accepted (default=None)
        fastdmatype -- Moving average type for the fastdmatype moving average.
        By default, fastmatype=0. Integers 0 - 8 are accepted
        (check  down the mappings) or the string containing the math type can
        also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "STOCHF"
        url = "{}function={}&symbol={}&interval={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval)
        if fastkperiod:
            url="{}&fastkperiod={}".format(url,fastkperiod)
        if fastdperiod:
            url="{}&fastdperiod={}".format(url, fastdperiod)
        if fastdmatype:
            # Check if it is an integer or a string
            try:
                value = int(fastdmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(fastdmatype)
            url="{}&fastdmatype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: STOCHF',
        'Meta Data')

    def get_rsi(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the relative strength index time series in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "RSI"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: RSI','Meta Data')

    def get_stochrsi(self, symbol, interval='60min', time_period=20,
    series_type='close', fastkperiod=None, fastdperiod=None, fastdmatype=None):
        """ Return the stochatic relative strength index in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastkperiod -- The time period of the fastk moving average. Positive
        integers are accepted (default=None)
        fastdperiod -- The time period of the fastd moving average. Positive
        integers are accepted (default=None)
        fastdmatype -- Moving average type for the fastdmatype moving average.
        By default, fastmatype=0. Integers 0 - 8 are accepted
        (check  down the mappings) or the string containing the math type can
        also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "STOCHRSI"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type)
        if fastkperiod:
            url="{}&fastkperiod={}".format(url,fastkperiod)
        if fastdperiod:
            url="{}&fastdperiod={}".format(url, fastdperiod)
        if fastdmatype:
            # Check if it is an integer or a string
            try:
                value = int(fastdmatype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(fastdmatype)
            url="{}&fastdmatype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: STOCHRSI',
        'Meta Data')

    def get_willr(self, symbol, interval='60min', time_period=20):
        """ Return the Williams' %R (WILLR) values in two json objects as data
        and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "WILLR"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, self.key)
        return self._handle_api_call(url,'Technical Analysis: WILLR','Meta Data')

    def get_adx(self, symbol, interval='60min', time_period=20):
        """ Return  the average directional movement index values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "ADX"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, self.key)
        return self._handle_api_call(url,'Technical Analysis: ADX','Meta Data')

    def get_adxr(self, symbol, interval='60min', time_period=20):
        """ Return  the average directional movement index  rating in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "ADXR"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, self.key)
        return self._handle_api_call(url,'Technical Analysis: ADXR','Meta Data')

    def get_apo(self, symbol, interval='60min', series_type='close',
    fastperiod=None, slowperiod=None, matype=None):
        """ Return the absolute price oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min'
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastperiod -- Positive integers are accepted (default=None)
        slowperiod -- Positive integers are accepted (default=None)
        matype     -- Moving average type. By default, fastmatype=0.
        Integers 0 - 8 are accepted (check  down the mappings) or the string
        containing the math type can also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "APO"
        url = "{}function={}&symbol={}&interval={}&series_type={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval,
        series_type)
        if fastperiod:
            url="{}&fastperiod={}".format(url,fastperiod)
        if slowperiod:
            url="{}&slowperiod={}".format(url, slowperiod)
        if matype:
            # Check if it is an integer or a string
            try:
                value = int(matype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(matype)
            url="{}&matype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: APO','Meta Data')

    def get_ppo(self, symbol, interval='60min', series_type='close',
    fastperiod=None, slowperiod=None, matype=None):
        """ Return the percentage price oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min'
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastperiod -- Positive integers are accepted (default=None)
        slowperiod -- Positive integers are accepted (default=None)
        matype     -- Moving average type. By default, fastmatype=0.
        Integers 0 - 8 are accepted (check  down the mappings) or the string
        containing the math type can also be used.

        0 = Simple Moving Average (SMA),
        1 = Exponential Moving Average (EMA),
        2 = Weighted Moving Average (WMA),
        3 = Double Exponential Moving Average (DEMA),
        4 = Triple Exponential Moving Average (TEMA),
        5 = Triangular Moving Average (TRIMA),
        6 = T3 Moving Average,
        7 = Kaufman Adaptive Moving Average (KAMA),
        8 = MESA Adaptive Moving Average (MAMA)
        """
        _FUNCTION_KEY = "PPO"
        url = "{}function={}&symbol={}&interval={}&series_type={}".format(
        AlphaVantage._ALPHA_VANTAGE_API_URL,_FUNCTION_KEY, symbol, interval,
        series_type)
        if fastperiod:
            url="{}&fastperiod={}".format(url,fastperiod)
        if slowperiod:
            url="{}&slowperiod={}".format(url, slowperiod)
        if matype:
            # Check if it is an integer or a string
            try:
                value = int(matype)
            except ValueError:
                value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(matype)
            url="{}&matype={}".format(url, value)
        url = "{}&apikey={}".format(url, self.key)
        return self._handle_api_call(url,'Technical Analysis: PPO','Meta Data')

    def get_mom(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the momentum values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "MOM"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: MOM','Meta Data')

    def get_bop(self, symbol, interval='60min', time_period=20):
        """ Return the balance of power values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "BOP"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, self.key)
        return self._handle_api_call(url,'Technical Analysis: BOP','Meta Data')

    def get_cci(self, symbol, interval='60min', time_period=20):
        """ Return the commodity channel index values  in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "CCI"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, self.key)
        return self._handle_api_call(url,'Technical Analysis: CCI','Meta Data')

    def get_cmo(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the Chande momentum oscillator in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "CMO"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: CMO','Meta Data')

    def get_roc(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the rate of change values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "ROC"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: ROC','Meta Data')

    def get_rocr(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the rate of change ratio values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "ROCR"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: ROCR','Meta Data')

    def get_aroon(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the aroon values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "AROON"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: AROON','Meta Data')

    def get_aroonosc(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the aroon oscillator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "AROONOSC"
        url = "{}function={}&symbol={}&interval={}&time_period={}"\
        "&series_type={}&apikey={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
        _FUNCTION_KEY, symbol, interval, time_period, series_type, self.key)
        return self._handle_api_call(url,'Technical Analysis: AROONOSC','Meta Data')

if __name__ == '__main__':
    av = AlphaVantage(key='486U')
    data, meta_data = av.get_sma('GOOGL')
    print(data)
