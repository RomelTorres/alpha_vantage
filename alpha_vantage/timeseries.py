from .alphavantage import AlphaVantage as av


class TimeSeries(av):

    """This class implements all the api calls to times series
    """
    @av._output_format
    @av._call_api_on_func
    def get_intraday(self, symbol, interval='15min', outputsize='compact', month=''):
        """ Return intraday time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min'
                (default '15min')
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length intraday times
                series, commonly above 1MB (default 'compact')
            month:  The specified month of targeted time series. By default, the latest
                month available in the API is returned. Strings should be in the format
                YYYY-MM (e.g. 2021-07) (default '')
        """
        _FUNCTION_KEY = "TIME_SERIES_INTRADAY"
        return _FUNCTION_KEY, "Time Series ({})".format(interval), 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_daily(self, symbol, outputsize='compact'):
        """ Return daily time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length daily times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = "TIME_SERIES_DAILY"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_daily_adjusted(self, symbol, outputsize='compact'):
        """ Return daily adjusted (date, daily open, daily high, daily low,
        daily close, daily split/dividend-adjusted close, daily volume)
        time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length daily times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = "TIME_SERIES_DAILY_ADJUSTED"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_weekly(self, symbol):
        """ Return weekly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        return _FUNCTION_KEY, 'Weekly Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_weekly_adjusted(self, symbol):
        """  weekly adjusted time series (last trading day of each week,
        weekly open, weekly high, weekly low, weekly close, weekly adjusted
        close, weekly volume, weekly dividend) of the equity specified,
        covering up to 20 years of historical data.
        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY_ADJUSTED"
        return _FUNCTION_KEY, 'Weekly Adjusted Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_monthly(self, symbol):
        """ Return monthly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        return _FUNCTION_KEY, 'Monthly Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_monthly_adjusted(self, symbol):
        """ Return monthly time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY_ADJUSTED"
        return _FUNCTION_KEY, 'Monthly Adjusted Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_quote_endpoint(self, symbol):
        """ Return the latest price and volume information for a
         security of your choice

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data

        """
        _FUNCTION_KEY = "GLOBAL_QUOTE"
        return _FUNCTION_KEY, 'Global Quote', None

    @av._output_format
    @av._call_api_on_func
    def get_symbol_search(self, keywords):
        """ Return best matching symbols and market information
        based on keywords. It raises ValueError when problems arise

        Keyword Arguments:
            keywords: the keywords to query on

        """
        _FUNCTION_KEY = "SYMBOL_SEARCH"
        return _FUNCTION_KEY, 'bestMatches', None
