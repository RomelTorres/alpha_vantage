import inspect
import os
import sys
from functools import wraps

# Pandas became an optional dependency, but we still want to track it
from helpers.baseurlsession import BaseURLSession

try:
    import pandas
    
    _PANDAS_FOUND = True
except ImportError:
    _PANDAS_FOUND = False
import csv


class AlphaVantage(object):
    """Base class containing the session. Is subclassed by other classes.
    """
    _ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"
    _ALPHA_VANTAGE_MATH_MAP = ['SMA', 'EMA', 'WMA', 'DEMA', 'TEMA', 'TRIMA',
                               'T3', 'KAMA', 'MAMA']
    _ALPHA_VANTAGE_DIGITAL_CURRENCY_LIST = \
        "https://www.alphavantage.co/digital_currency_list/"
    
    _RAPIDAPI_URL = "https://alpha-vantage.p.rapidapi.com/query"
    
    def __init__(self, key: str = None, output_format: str = 'json',
                 treat_info_as_error: bool = True, indexing_type: str = 'date', proxy: dict = None,
                 rapidapi: bool = False):
        """Initialize the class.

        Keyword Arguments:
            key:  Alpha Vantage API key.
            treat_info_as_error: Treat information from the API as errors.
            output_format:  Specifies the output format directed to the user.
            Either 'json', 'pandas' os 'csv'.
            indexing_type: Either 'date' to use the default date string given
            by the alpha vantage api call or 'integer' if you just want an
            integer indexing on your dataframe. Only valid, when the
            output_format is 'pandas'.
            proxy: Dictionary mapping protocol or protocol and hostname to
            the URL of the proxy.
            rapidapi: Boolean describing whether or not the API key is
            through the RapidAPI platform or not.
        """
        if key is None:
            key = os.getenv('ALPHAVANTAGE_API_KEY')
        if not key or not isinstance(key, str):
            raise ValueError('The AlphaVantage API key must be provided '
                             'either through the key parameter or '
                             'through the environment variable '
                             'ALPHAVANTAGE_API_KEY. Get a free key '
                             'from the AlphaVantage website: '
                             'https://www.alphavantage.co/support/#api-key')
        
        # Session preparation
        # Set RapidAPI-specific URL and Headers.
        self._create_session(rapidapi)
        
        if rapidapi:
            self.session.headers['x-rapidapi-host'] = "alpha-vantage.p.rapidapi.com"
            self.session.headers['x-rapidapi-key'] = key
        # Set AlphaVantage-specific URL and Headers.
        else:
            self.session.params['apikey'] = key
        
        # Add proxy if specified
        self.session.proxies = proxy or {}
        
        # Storage of further arguments
        self.output_format = output_format.lower()
        if self.output_format == 'pandas' and not _PANDAS_FOUND:
            raise ValueError("The pandas library was not found, therefore can "
                             "not be used as an output format, please install "
                             "manually")
        self.treat_info_as_error = treat_info_as_error
        
        # Not all the calls accept a data type appended at the end, this
        # variable will be overridden by those functions not needing it.
        self._append_type = True
        self.indexing_type = indexing_type.lower()
    
    def close(self):
        """Closes the underlying session."""
        self.session.close()
    
    def _create_session(self, rapidapi: bool):
        """Creates a session."""
        if rapidapi:
            self.session = BaseURLSession(AlphaVantage._RAPIDAPI_URL)
        else:
            self.session = BaseURLSession(AlphaVantage._ALPHA_VANTAGE_API_URL)
    
    def set_proxy(self, proxy=None):
        """Set a new proxy configuration
    
        Keyword Arguments:
            proxy: Dictionary mapping protocol or protocol and hostname to
            the URL of the proxy.
        """
        self.session.proxies = proxy or {}
    
    def map_to_matype(self, matype):
        """Convert to the AlphaVantage math type integer. It returns an
        integer correspondent to the type of math to apply to a function. It
        raises ValueError if an integer greater than the supported math types
        is given.
    
        Keyword Arguments:
            matype:  The math type of the AlphaVantage API. It accepts
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
    
    def _handle_api_call(self, params, override=None):
        """Handle the return call from the API. It raises a ValueError on problems.
        Allows to override the data type that is requested/expected from the API.
    
        Keyword Arguments:
            params:  The parameters to the service.
            override: The datatype to use instead of the class specified one.
        """
        # Override output format
        output_format = self.output_format
        if override is not None:
            output_format = override
            if 'datatype' in params:
                # 'pandas' is no datatype that is supported by the AlphaVantage API
                # to be consistent with other data type arguments this is converted
                # to 'json'.
                if 'pandas' == override:
                    override = 'json'
                
                params['datatype'] = override
        
        response = self.session.get('', params=params)
        
        # Handle response
        if 'json' == output_format or \
                'pandas' == output_format:
            return self._handle_json_response(response.json())
        elif 'csv' == output_format:
            return self._handle_csv_response(response.text)
        else:
            raise NotImplementedError(
                'Handling of data type {} is not yet supported.'.format(output_format))
    
    def _handle_json_response(self, json_response):
        if not json_response:
            raise ValueError('Error getting data from the API, no return was given.')
        
        elif "Error Message" in json_response:
            raise ValueError(json_response["Error Message"])
        
        elif "Information" in json_response and self.treat_info_as_error:
            raise ValueError(json_response["Information"])
        
        elif "Note" in json_response and self.treat_info_as_error:
            raise ValueError(json_response["Note"])
        
        return json_response
    
    def _handle_csv_response(self, text_response):
        csv_response = csv.reader(text_response.splitlines())
        if not csv_response:
            raise ValueError('Error getting data from the API, no return was given.')
        return csv_response
    
    class call_api_on_func(object):
        """Decorator for forming the API call with the arguments of the
        function, it works by taking the arguments given to the function
        and building the url to call the api on it. Allows overriding the
        requested/expected output format of the API call.
        """
        
        def __init__(self, override: str = None) -> None:
            """Initializes this decorator with the override argument."""
            super().__init__()
            self.override = override
        
        def __call__(cls, func):
            """The decorator logic, is called before decorated functions
            are executed.
            
            Keyword Arguments:
                func: The function to be decorated
            """
            argspec, positional_count, defaults = cls._handle_arguments(func)
            
            # Actual decorating
            @wraps(func)
            def _call_wrapper(self, *args, **kwargs):
                used_kwargs = cls._process_kwargs(args, kwargs, argspec, positional_count, defaults)
                
                # Form the base url, the original function called must return
                # the function name defined in the AlphaVantage API and the data
                # key for it and for its meta data.
                function_name, data_key, meta_data_key = func(self, *args, **kwargs)
                
                params = cls._create_parameters(self, function_name, argspec, args, used_kwargs)
                
                return self._handle_api_call(params, cls.override), data_key, meta_data_key
            
            return _call_wrapper
        
        def _create_parameters(cls, self, function_name, argspec, args, used_kwargs):
            # Create parameter dict
            params = {
                'function': function_name
            }
            
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
                    
                    params[arg_name] = arg_value
            
            # Allow the output format to be JSON or CSV (supported by the
            # AlphaVantage API). Pandas is simply converted JSON.
            if 'json' == self.output_format.lower() or \
                    'csv' == self.output_format.lower():
                oformat = self.output_format.lower()
            elif 'pandas' == self.output_format.lower():
                oformat = 'json'
            else:
                raise ValueError("Output format: {} not recognized, only 'json',"
                                 "'pandas' and 'csv' are supported".format(
                    self.output_format.lower()))
            
            if self._append_type:
                params['datatype'] = oformat if cls.override is None else cls.override
            
            return params
        
        def _handle_arguments(self, func):
            # Argument Handling
            if sys.version_info[0] < 3:
                # Deprecated since version 3.0
                argspec = inspect.getargspec(func)
            else:
                argspec = inspect.getfullargspec(func)
            
            try:
                # Assume most of the cases have a mixed between args and named
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
            
            return argspec, positional_count, defaults
        
        def _process_kwargs(self, args, kwargs, argspec, positional_count, defaults):
            used_kwargs = kwargs.copy()
            
            # Get the used positional arguments given to the function
            used_kwargs.update(zip(argspec.args[positional_count:],
                                   args[positional_count:]))
            
            # Update the dictionary to include the default parameters from the
            # function
            used_kwargs.update({k: used_kwargs.get(k, d)
                                for k, d in defaults.items()})
            
            return used_kwargs
    
    class output_format(object):
        """Decorator that processes the response output to conform to the
        requested data type. The data type can also be overridden.
    
        Keyword Arguments:
            override:  Override the output format. Either 'json', 'pandas' or 'csv'.
        """
        
        def __init__(self, override: str = None, formatting: str = 'default') -> None:
            super().__init__()
            self.override = override
            self.formatting = formatting
        
        def __call__(cls, func):
            @wraps(func)
            def _format_wrapper(self, *args, **kwargs):
                call_response, data_key, meta_data_key = func(self, *args, **kwargs)
                
                return cls._handle_call_response(self, call_response, data_key, meta_data_key)
            
            return _format_wrapper
        
        def _handle_call_response(cls, self, call_response, data_key, meta_data_key):
            """Handles the call response of the wrapped function in __call__."""
            api_format = 'csv' if isinstance(call_response, type(csv.reader(''))) else 'json'
            
            # Override of the output format
            if cls.override is None:
                output_format = self.output_format.lower()
            else:
                output_format = cls.override.lower()
            
            if 'json' == api_format:
                # Formatting for sector performance
                if 'sector' == cls.formatting:
                    if isinstance(data_key, list):
                        data = {key: {k: cls._percentage_to_float(v) for k, v in
                                      call_response[key].items()} for key in data_key}
                
                elif 'default' == cls.formatting:
                    if data_key is not None:
                        data = call_response[data_key]
                    else:
                        data = call_response
                
                if meta_data_key is not None:
                    meta_data = call_response[meta_data_key]
                else:
                    meta_data = None
                
                if 'json' == output_format:
                    return data, meta_data
                elif 'pandas' == output_format or \
                        'csv' == output_format:
                    if isinstance(data, list):
                        data_pandas = pandas.DataFrame(data)
                    else:
                        try:
                            data_pandas = pandas.DataFrame.from_dict(data,
                                                                     orient='index',
                                                                     dtype='float')
                        # This is for Global quotes or any other new Alpha Vantage
                        # data that is added.
                        # It will have to be updated so that we can get exactly
                        # The dataframes we want moving forward
                        except ValueError:
                            data = {data_key: data}
                            data_pandas = pandas.DataFrame.from_dict(data,
                                                                     orient='index',
                                                                     dtype='object')
                            return data_pandas, meta_data
                    
                    data_pandas = cls._convert_pandas_index(self, data_pandas)
                    
                    if 'pandas' == output_format:
                        return data_pandas, meta_data
                    else:
                        # JSON to CSV conversion through Pandas.
                        # Convert to CSV reader to stay consistent with native CSV API call.
                        return csv.reader(data_pandas.to_csv().splitlines())
            elif 'csv' == api_format:
                if 'pandas' == output_format or \
                        'json' == output_format:
                    # Converts the CSV reader to a format that can be read by pandas
                    # directly
                    data_list = list(call_response)
                    data_pandas = pandas.DataFrame.from_records(data_list[1:],
                                                                columns=data_list[0])
                    
                    data_pandas = cls._convert_pandas_index(self, data_pandas)
                    
                    if 'pandas' == output_format:
                        return data_pandas, None
                    else:
                        return data_pandas.to_json(), None
                else:
                    return call_response, None
        
        def _convert_pandas_index(self, av, data_pandas: pandas.DataFrame):
            """Converts the index of a pandas.DataFrame as specified in the AlphaVantage class."""
            if not isinstance(data_pandas.index, pandas.RangeIndex) and \
                    'integer' == av.indexing_type and 'default' == self.formatting:
                # Set Date/Time as an actual column so a new numerical index
                # will be created, but only when specified by the user.
                data_pandas.reset_index(level=0, inplace=True)
                data_pandas.rename(columns={'index': 'date'}, inplace=True)
                data_pandas.index.name = 'index'
            elif not isinstance(data_pandas.index, pandas.DatetimeIndex) and \
                    'date' == av.indexing_type and 'default' == self.formatting:
                # TODO check if index is actually a date(time) and only convert if this is the case
                if 'time' in data_pandas.columns:
                    data_pandas.index = data_pandas.time
                    data_pandas.drop(columns=['time'], inplace=True)
                data_pandas.index = pandas.to_datetime(data_pandas.index)
            
            return data_pandas
        
        def _percentage_to_float(self, val):
            """Transform a string of the form f.f% into f.f/100
    
            Keyword Arguments:
                val: The string to convert
            """
            return float(val.strip('%')) / 100
