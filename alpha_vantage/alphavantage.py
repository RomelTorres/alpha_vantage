try:
    # Python 3 import
    from urllib.request import urlopen
except ImportError:
    # Python 2.* import
    from urllib2 import urlopen

from simplejson import loads
from functools import wraps
import inspect


class AlphaVantage:
    """
        This class is in charge of creating a python interface between the Alpha
        Vantage restful API and your python application
    """
    _ALPHA_VANTAGE_API_URL = "http://www.alphavantage.co/query?"
    _ALPHA_VANTAGE_MATH_MAP = ['SMA','EMA','WMA','DEMA','TEMA', 'TRIMA','T3',
    'KAMA','MAMA']

    def __init__(self, key=None, retries=3):
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
        @wraps(func)
        def _retry_wrapper(self, *args, **kwargs):
            for retry in range(self.retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except ValueError as err:
                    pass
            raise ValueError(err)
        return _retry_wrapper


    def _call_api_on_func(func):
        """ Decorator for forming the api call with the arguments of the
        function, it works by taking the arguments given to the function
        and building the url to call the api on it

        Keyword arguments:
        func -- The function to be decorated
        """
        argspec = inspect.getargspec(func)
        try:
            # Asumme most of the cases have a mixed between args and named
            # args
            positional_count = len(argspec.args) - len(argspec.defaults)
            defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
        except TypeError:
            if argspec.args:
                # No defaults
                positional_count = len(argspec.args)
                defaults = {}
            elif argspec.defaults:
                # Only defaults
                positional_count = 0
                defaults = argspec.defaults

        @wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            used_kwargs = kwargs.copy()
            # Get the used positional arguments given to the function
            used_kwargs.update(zip(argspec.args[positional_count:],
            args[positional_count:]))
            # Update the dictionary to include the default parameters from the
            # function
            used_kwargs.update({k: used_kwargs.get(k, d)
            for k, d in defaults.items()})
            # Form the base url, the original function called must return
            # the function name defined in the alpha vantage api and the data
            # key for it and for its meta data.
            function_name, data_key, meta_data_key = func(self, *args, **kwargs)
            url = "{}function={}".format(AlphaVantage._ALPHA_VANTAGE_API_URL,
            function_name)
            for idx, arg_name in enumerate(argspec.args[1:]):
                try:
                    arg_value = args[idx]
                except IndexError:
                    arg_value = used_kwargs[arg_name]
                if 'matype' in arg_name and arg_value:
                    # If the argument name has matype, we gotta map the string
                    # or the integer
                    arg_value = self.map_to_matype(arg_value)
                if arg_value:
                    # Discard argument in the url formation if it was set to
                    # None (in other words, this will call the api with its
                    # internal defined parameter)
                    url = '{}&{}={}'.format(url, arg_name, arg_value)
            url='{}&apikey={}'.format(url, self.key)
            return self._handle_api_call(url, data_key, meta_data_key)
        return _call_wrapper

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

    def map_to_matype(self, matype):
        """ Convert to the alpha vantage math type integer. It returns an
        integer correspondant to the type of math to apply to a function. It
        raises ValueError if an integer greater than the supported math types
        is given.

        Keyword arguments
        matype -- The math type of the alpha vantage api. It accepts integers
        or a string representing the math type.

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
        # Check if it is an integer or a string
        try:
            value = int(matype)
            if abs(value) > len(AlphaVantage._ALPHA_VANTAGE_MATH_MAP):
                raise ValueError("The value {} is not supported".format(value))
        except ValueError:
            value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(matype)
        return value

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

    @_call_api_on_func
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
        return _FUNCTION_KEY, "Time Series ({})".format(interval), 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @_call_api_on_func
    def get_weekly(self, symbol):
        """ Return weekly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        return _FUNCTION_KEY, 'Weekly Time Series', 'Meta Data'

    @_call_api_on_func
    def get_monthly(self, symbol):
        """ Return monthly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        return _FUNCTION_KEY, 'Monthly Time Series', 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: SMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: EMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: WMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: DEMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: TEMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: TRIMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: KAMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: MAMA','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: T3','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: MACD','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: MACDEXT', 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: STOCH', 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: STOCHF', 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: RSI','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY, 'Technical Analysis: STOCHRSI', 'Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: WILLR','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: ADX','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: ADXR','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: APO','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: PPO','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: MOM','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: BOP','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: CCI','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: CMO','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: ROC','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: ROCR','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: AROON','Meta Data'

    @_call_api_on_func
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
        return _FUNCTION_KEY,'Technical Analysis: AROONOSC','Meta Data'

    @_call_api_on_func
    def get_mfi(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the money flow index values in two json
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
        _FUNCTION_KEY = "MFI"
        return _FUNCTION_KEY,'Technical Analysis: MFI','Meta Data'

    @_call_api_on_func
    def get_trix(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the1-day rate of change of a triple smooth exponential
        moving average in two json objects as data and meta_data.
        It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "TRIX"
        return _FUNCTION_KEY,'Technical Analysis: TRIX','Meta Data'

    @_call_api_on_func
    def get_ultsoc(self, symbol, interval='60min', timeperiod1=None,
    timeperiod2=None, timeperiod3=None):
        """ Return the ultimate oscillaror values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        timeperiod1 -- The first time period indicator. Positive integers are
        accepted. By default, timeperiod1=7
        timeperiod2 -- The first time period indicator. Positive integers are
        accepted. By default, timeperiod2=14
        timeperiod3 -- The first time period indicator. Positive integers are
        accepted. By default, timeperiod3=28
        """
        _FUNCTION_KEY = "ULTOSC"
        return _FUNCTION_KEY,'Technical Analysis: ULTOSC','Meta Data'

    @_call_api_on_func
    def get_dx(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the directional movement index values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "DX"
        return _FUNCTION_KEY,'Technical Analysis: DX','Meta Data'

    @_call_api_on_func
    def get_minus_di(self, symbol, interval='60min', time_period=20):
        """ Return the minus directional indicator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "MINUS_DI"
        return _FUNCTION_KEY,'Technical Analysis: MINUS_DI','Meta Data'

    @_call_api_on_func
    def get_plus_di(self, symbol, interval='60min', time_period=20):
        """ Return the plus directional indicator values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "PLUS_DI"
        return _FUNCTION_KEY,'Technical Analysis: PLUS_DI','Meta Data'

    @_call_api_on_func
    def get_minus_dm(self, symbol, interval='60min', time_period=20):
        """ Return the minus directional movement values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "MINUS_DM"
        return _FUNCTION_KEY,'Technical Analysis: MINUS_DM','Meta Data'

    @_call_api_on_func
    def get_plus_dm(self, symbol, interval='60min', time_period=20):
        """ Return the plus directional movement values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "PLUS_DM"
        return _FUNCTION_KEY,'Technical Analysis: PLUS_DM','Meta Data'

    @_call_api_on_func
    def get_bbands(self, symbol, interval='60min', time_period=20,  series_type='close',
    nbdevup=None, nbdevdn=None, matype=None):
        """ Return the bollinger bands values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min'
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        nbdevup -- The standard deviation multiplier of the upper band. Positive
        integers are accepted as default (default=2)
        nbdevdn -- The standard deviation multiplier of the lower band. Positive
        integers are accepted as default (default=2)
        matype  -- Moving average type. By default, matype=0.
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
        _FUNCTION_KEY = "BBANDS"
        return _FUNCTION_KEY,'Technical Analysis: BBANDS','Meta Data'

    @_call_api_on_func
    def get_midpoint(self, symbol, interval='60min', time_period=20, series_type='close'):
        """ Return the midpoint values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "MIDPOINT"
        return _FUNCTION_KEY,'Technical Analysis: MIDPOINT','Meta Data'

    @_call_api_on_func
    def get_midprice(self, symbol, interval='60min', time_period=20):
        """ Return the midprice values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        """
        _FUNCTION_KEY = "MIDPRICE"
        return _FUNCTION_KEY,'Technical Analysis: MIDPRICE','Meta Data'

    @_call_api_on_func
    def get_sar(self, symbol, interval='60min', acceleration=None, maximum=None):
        """ Return the midprice values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        acceleration -- The acceleration factor. Positive floats are accepted (
        default 0.01)
        maximum -- The acceleration factor maximum value. Positive floats
        are accepted (default 0.20 )
        """
        _FUNCTION_KEY = "SAR"
        return _FUNCTION_KEY,'Technical Analysis: SAR','Meta Data'

    @_call_api_on_func
    def get_trange(self, symbol, interval='60min'):
        """ Return the true range values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "TRANGE"
        return _FUNCTION_KEY,'Technical Analysis: TRANGE','Meta Data'

    @_call_api_on_func
    def get_atr(self, symbol, interval='60min', time_period=20):
        """ Return the average true range values in two json objects as
        data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        """
        _FUNCTION_KEY = "ATR"
        return _FUNCTION_KEY,'Technical Analysis: ATR','Meta Data'

    @_call_api_on_func
    def get_natr(self, symbol, interval='60min', time_period=20):
        """ Return the normalized average true range values in two json objects
        as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        time_period -- How many data points to average (default 20)
        """
        _FUNCTION_KEY = "NATR"
        return _FUNCTION_KEY,'Technical Analysis: NATR','Meta Data'

    @_call_api_on_func
    def get_ad(self, symbol, interval='60min'):
        """ Return the Chaikin A/D line values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "AD"
        return _FUNCTION_KEY,'Technical Analysis: Chaikin A/D','Meta Data'

    @_call_api_on_func
    def get_adosc(self, symbol, interval='60min', fastperiod=None,
    slowperiod=None):
        """ Return the Chaikin A/D oscillator values in two
        json objects as data and meta_data. It raises ValueError when problems
        arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min'
        fastperiod -- Positive integers are accepted (default=None)
        slowperiod -- Positive integers are accepted (default=None)
        """
        _FUNCTION_KEY = "ADOSC"
        return _FUNCTION_KEY,'Technical Analysis: ADOSC','Meta Data'

    @_call_api_on_func
    def get_obv(self, symbol, interval='60min'):
        """ Return the on balance volume values in two json
        objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        """
        _FUNCTION_KEY = "OBV"
        return _FUNCTION_KEY,'Technical Analysis: OBV','Meta Data'

    @_call_api_on_func
    def get_ht_trendline(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, instantaneous trendline values in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_TRENDLINE"
        return _FUNCTION_KEY,'Technical Analysis: HT_TRENDLINE','Meta Data'

    @_call_api_on_func
    def get_ht_sine(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, sine wave values in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_SINE"
        return _FUNCTION_KEY,'Technical Analysis: HT_SINE','Meta Data'

    @_call_api_on_func
    def get_ht_trendmode(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, trend vs cycle mode in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_TRENDMODE"
        return _FUNCTION_KEY,'Technical Analysis: HT_TRENDMODE','Meta Data'

    @_call_api_on_func
    def get_ht_dcperiod(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, dominant cycle period in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_DCPERIOD"
        return _FUNCTION_KEY,'Technical Analysis: HT_DCPERIOD','Meta Data'

    @_call_api_on_func
    def get_ht_dcphase(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, dominant cycle phase in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_DCPHASE"
        return _FUNCTION_KEY,'Technical Analysis: HT_DCPHASE','Meta Data'

    @_call_api_on_func
    def get_ht_phasor(self, symbol, interval='60min', series_type='close'):
        """ Return the Hilbert transform, phasor components in two
        json objects as data and meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
        'weekly', 'monthly' (default '60min')
        series_type -- The desired price type in the time series. Four types
        are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "HT_PHASOR"
        return _FUNCTION_KEY, 'Technical Analysis: HT_PHASOR', 'Meta Data'

if __name__ == '__main__':
    av = AlphaVantage(key='486U')
    print(av.get_intraday(symbol='GOOGL',interval='1min'))
