from .alphavantage import AlphaVantage as av


class TimesSeries(av):
    """This class implements all the api calls to times series
    """
    @av._output_format
    @av._call_api_on_func
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

    @av._output_format
    @av._call_api_on_func
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

    @av._output_format
    @av._call_api_on_func
    def get_weekly(self, symbol):
        """ Return weekly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        return _FUNCTION_KEY, 'Weekly Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_monthly(self, symbol):
        """ Return monthly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        return _FUNCTION_KEY, 'Monthly Time Series', 'Meta Data'
