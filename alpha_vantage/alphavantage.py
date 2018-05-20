import requests
import os
from functools import wraps
import inspect
# Pandas became an optional dependency, but we still want to track it
try:
    import pandas
    _PANDAS_FOUND = True
except ImportError:
    _PANDAS_FOUND = False
import csv


class AlphaVantage(object):
    """ Base class where the decorators and base function for the other
    classes of this python wrapper will inherit from.
    """
    _ALPHA_VANTAGE_API_URL = "http://www.alphavantage.co/query?"
    _ALPHA_VANTAGE_MATH_MAP = ['SMA', 'EMA', 'WMA', 'DEMA', 'TEMA', 'TRIMA',
                               'T3', 'KAMA', 'MAMA']
    _ALPHA_VANTAGE_DIGITAL_CURRENCY_LIST = \
        "https://www.alphavantage.co/digital_currency_list/"

    def __init__(self, key=None, retries=5, output_format='json',
                 treat_info_as_error=True, indexing_type='date', proxy=None):
        """ Initialize the class

        Keyword Arguments:
            key:  Alpha Vantage api key
            retries:  Maximum amount of retries in case of faulty connection or
                server not able to answer the call.
            treat_info_as_error: Treat information from the api as errors
            output_format:  Either 'json', 'pandas' os 'csv'
            indexing_type: Either 'date' to use the default date string given
            by the alpha vantage api call or 'integer' if you just want an
            integer indexing on your dataframe. Only valid, when the
            output_format is 'pandas'
            proxy: Dictionary mapping protocol or protocol and hostname to 
            the URL of the proxy.
        """
        if key is None:
            key = os.getenv('ALPHAVANTAGE_API_KEY')
        if not key or not isinstance(key, str):
            raise ValueError('The AlphaVantage API key must be provided '
                             'either through the key parameter or '
                             'through the environment variable '
                             'ALPHAVANTAGE_API_KEY. Get a free key '
                             'from the alphavantage website: '
                             'https://www.alphavantage.co/support/#api-key')
        self.key = key
        self.retries = retries
        self.output_format = output_format
        if self.output_format is 'pandas' and not _PANDAS_FOUND:
            raise ValueError("The pandas library was not found, therefore can "
                             "not be used as an output format, please install "
                             "manually")
        self.treat_info_as_error = treat_info_as_error
        # Not all the calls accept a data type appended at the end, this
        # variable will be overriden by those functions not needing it.
        self._append_type = True
        self.indexing_type = indexing_type
        self.proxy = proxy or {}

    def _retry(func):
        """ Decorator for retrying api calls (in case of errors from the api
        side in bringing the data)

        Keyword Arguments:
            func:  The function to be retried
        """
        @wraps(func)
        def _retry_wrapper(self, *args, **kwargs):
            error_message = ""
            for retry in range(self.retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except ValueError as err:
                    error_message = str(err)
            raise ValueError(str(error_message))
        return _retry_wrapper

    @classmethod
    def _call_api_on_func(cls, func):
        """ Decorator for forming the api call with the arguments of the
        function, it works by taking the arguments given to the function
        and building the url to call the api on it

        Keyword Arguments:
            func:  The function to be decorated
        """

        # Argument Handling
        argspec = inspect.getargspec(func)
        try:
            # Asumme most of the cases have a mixed between args and named
            # args
            positional_count = len(argspec.args) - len(argspec.defaults)
            defaults = dict(
                zip(argspec.args[positional_count:], argspec.defaults))
        except TypeError:
            if argspec.args:
                # No defaults
                positional_count = len(argspec.args)
                defaults = {}
            elif argspec.defaults:
                # Only defaults
                positional_count = 0
                defaults = argspec.defaults
        # Actual decorating

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
            function_name, data_key, meta_data_key = func(
                self, *args, **kwargs)
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
                    if isinstance(arg_value, tuple) or isinstance(arg_value, list):
                        # If the argument is given as list, then we have to
                        # format it, you gotta format it nicely
                        arg_value = ','.join(arg_value)
                    url = '{}&{}={}'.format(url, arg_name, arg_value)
            # Allow the output format to be json or csv (supported by
            # alphavantage api). Pandas is simply json converted.
            if 'json' in self.output_format.lower() or 'csv' in self.output_format.lower():
                oformat = self.output_format.lower()
            elif 'pandas' in self.output_format.lower():
                oformat = 'json'
            else:
                raise ValueError("Output format: {} not recognized, only json,"
                                 "pandas and csv are supported".format(
                                     self.output_format.lower()))
            if self._append_type:
                url = '{}&apikey={}&datatype={}'.format(url, self.key, oformat)
            else:
                url = '{}&apikey={}'.format(url, self.key)
            return self._handle_api_call(url), data_key, meta_data_key
        return _call_wrapper

    @classmethod
    def _output_format(cls, func, override=None):
        """ Decorator in charge of giving the output its right format, either
        json or pandas

        Keyword Arguments:
            func:  The function to be decorated
            override:  Override the internal format of the call, default None
        """
        @wraps(func)
        def _format_wrapper(self, *args, **kwargs):
            call_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            if 'json' in self.output_format.lower() or 'pandas' \
                    in self.output_format.lower():
                data = call_response[data_key]
                if meta_data_key is not None:
                    meta_data = call_response[meta_data_key]
                else:
                    meta_data = None
                # Allow to override the output parameter in the call
                if override is None:
                    output_format = self.output_format.lower()
                elif 'json' or 'pandas' in override.lower():
                    output_format = override.lower()
                # Choose output format
                if output_format == 'json':
                    return data, meta_data
                elif output_format == 'pandas':
                    if isinstance(data, list):
                        # If the call returns a list, then we will append them
                        # in the resulting data frame. If in the future
                        # alphavantage decides to do more with returning arrays
                        # this might become buggy. For now will do the trick.
                        data_array = []
                        for val in data:
                            data_array.append([v for _, v in val.items()])
                        data_pandas = pandas.DataFrame(data_array, columns=[
                            k for k, _ in data[0].items()])
                    else:
                        data_pandas = pandas.DataFrame.from_dict(data,
                                                                 orient='index',
                                                                 dtype=float)
                    data_pandas.index.name = 'date'
                    if 'integer' in self.indexing_type:
                        # Set Date as an actual column so a new numerical index
                        # will be created, but only when specified by the user.
                        data_pandas.reset_index(level=0, inplace=True)
                    return data_pandas, meta_data
            elif 'csv' in self.output_format.lower():
                return call_response, None
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.output_format))
        return _format_wrapper

    def set_proxy(self, proxy=None):
        """ Set a new proxy configuration

        Keyword Arguments:
            proxy: Dictionary mapping protocol or protocol and hostname to 
            the URL of the proxy.
        """
        self.proxy = proxy or {}

    def map_to_matype(self, matype):
        """ Convert to the alpha vantage math type integer. It returns an
        integer correspondant to the type of math to apply to a function. It
        raises ValueError if an integer greater than the supported math types
        is given.

        Keyword Arguments:
            matype:  The math type of the alpha vantage api. It accepts
            integers or a string representing the math type.

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
        # Check if it is an integer or a string
        try:
            value = int(matype)
            if abs(value) > len(AlphaVantage._ALPHA_VANTAGE_MATH_MAP):
                raise ValueError("The value {} is not supported".format(value))
        except ValueError:
            value = AlphaVantage._ALPHA_VANTAGE_MATH_MAP.index(matype)
        return value

    @_retry
    def _handle_api_call(self, url):
        """ Handle the return call from the  api and return a data and meta_data
        object. It raises a ValueError on problems

        Keyword Arguments:
            url:  The url of the service
            data_key:  The key for getting the data from the jso object
            meta_data_key:  The key for getting the meta data information out
            of the json object
        """
        response = requests.get(url, proxies=self.proxy)
        if 'json' in self.output_format.lower() or 'pandas' in \
                self.output_format.lower():
            json_response = response.json()
            if "Error Message" in json_response:
                raise ValueError(json_response["Error Message"])
            elif "Information" in json_response and self.treat_info_as_error:
                raise ValueError(json_response["Information"])
            return json_response
        else:
            csv_response = csv.reader(response.text.splitlines())
            if not csv_response:
                raise ValueError(
                    'Error getting data from the api, no return was given.')
            return csv_response
