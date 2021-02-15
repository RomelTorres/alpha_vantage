from functools import wraps

# Pandas became an optional dependency, but we still want to track it
from helpers.asyncbaseurlsession import AsyncBaseURLSession
from ..alphavantage import AlphaVantage as AlphaVantageBase

try:
    import pandas
    
    _PANDAS_FOUND = True
except ImportError:
    _PANDAS_FOUND = False


class AlphaVantage(AlphaVantageBase):
    """Async version of the base class where the decorators and base function for
    the other classes of this python wrapper will inherit from.
    """
    
    async def close(self):
        """Close the underlying aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()
    
    def _create_session(self, rapidapi: bool):
        """Creates a session."""
        if rapidapi:
            self.session = AsyncBaseURLSession(AlphaVantage._RAPIDAPI_URL)
        else:
            self.session = AsyncBaseURLSession(AlphaVantage._ALPHA_VANTAGE_API_URL)
    
    async def _handle_api_call(self, params, override=None):
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
        
        response = await self.session.get('', params=params)
        
        # Handle response
        if 'json' == output_format or \
                'pandas' == output_format:
            return self._handle_json_response(await response.json())
        elif 'csv' == output_format:
            return self._handle_csv_response(await response.text())
        else:
            raise NotImplementedError(
                'Handling of data type {} is not yet supported.'.format(output_format))
    
    class _call_api_on_func(AlphaVantageBase._call_api_on_func):
        """Decorator for forming the API call with the arguments of the
        function, it works by taking the arguments given to the function
        and building the url to call the api on it. Allows overriding the
        requested/expected output format of the API call.
        """
        
        def __call__(cls, func):
            """The decorator logic, is called before decorated functions
            are executed.
            
            Keyword Arguments:
                func: The function to be decorated
            """
            argspec, positional_count, defaults = cls._handle_arguments(func)
            
            # Actual decorating
            @wraps(func)
            async def _call_wrapper(self, *args, **kwargs):
                used_kwargs = cls._process_kwargs(args, kwargs, argspec, positional_count, defaults)
                
                # Form the base url, the original function called must return
                # the function name defined in the AlphaVantage API and the data
                # key for it and for its meta data.
                function_name, data_key, meta_data_key = func(self, *args, **kwargs)
                
                params = cls._create_parameters(self, function_name, argspec, args, used_kwargs)
                
                return await self._handle_api_call(params, cls.override), data_key, meta_data_key
            
            return _call_wrapper
    
    class _output_format(AlphaVantageBase._output_format):
        """Decorator that processes the response output to conform to the
        requested data type. The data type can also be overridden.
    
        Keyword Arguments:
            override:  Override the output format. Either 'json', 'pandas' or 'csv'.
        """
        
        def __call__(cls, func):
            @wraps(func)
            async def _format_wrapper(self, *args, **kwargs):
                call_response, data_key, meta_data_key = await func(self, *args, **kwargs)
                
                return cls._handle_call_response(self, call_response, data_key, meta_data_key)
            
            return _format_wrapper
