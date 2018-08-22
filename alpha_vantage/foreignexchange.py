from .alphavantage import AlphaVantage as av


class ForeignExchange(av):
    """Realtime currency exchange rates for physical and digital currencies.
    """

    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments
        """
        super(ForeignExchange, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not compatible with the ForeignExchange class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_rate(self, from_currency, to_currency):
        """ Returns the realtime exchange rate for any pair of physical
        currency (e.g., EUR) or physical currency (e.g., USD).

        Keyword Arguments:
            from_currency: The currency you would like to get the exchange rate
            for. It can either be a physical currency or digital/crypto currency.
            For example: from_currency=USD or from_currency=BTC.
            to_currency: The destination currency for the exchange rate.
            It can either be a physical currency or digital/crypto currency.
            For example: to_currency=USD or to_currency=BTC.
        """
        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Realtime Currency Exchange Rate', None

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_intraday(self, from_symbol, to_symbol, interval='15min', outputsize='compact'):
        """ Returns the intraday exchange rate for any pair of physical
        currency (e.g., EUR) or physical currency (e.g., USD).

        Keyword Arguments:
            from_symbol: The currency you would like to get the exchange rate
                for.
                For example: from_currency=EUR or from_currency=USD.
            to_symbol: The destination currency for the exchange rate.
                For example: to_currency=USD or to_currency=JPY.
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min'
                (default '15min')
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length intraday times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = 'FX_INTRADAY'
        return _FUNCTION_KEY, "Time Series FX ({})".format(interval), 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_daily(self, from_symbol, to_symbol, outputsize='compact'):
        """ Returns the daily exchange rate for any pair of physical
        currency (e.g., EUR) or physical currency (e.g., USD).

        Keyword Arguments:
            from_symbol: The currency you would like to get the exchange rate
                for.
                For example: from_symbol=EUR or from_symbol=USD.
            to_symbol: The destination currency for the exchange rate.
                For example: to_symbol=USD or to_symbol=JPY.
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length daily times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = 'FX_DAILY'
        return _FUNCTION_KEY, "Time Series FX (Daily)", 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_weekly(self, from_symbol, to_symbol, outputsize='compact'):
        """ Returns the weekly exchange rate for any pair of physical
        currency (e.g., EUR) or physical currency (e.g., USD).

        Keyword Arguments:
            from_symbol: The currency you would like to get the exchange rate
                for.
                For example: from_symbol=EUR or from_symbol=USD.
            to_symbol: The destination currency for the exchange rate.
                For example: to_symbol=USD or to_symbol=JPY.
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length weekly times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = 'FX_WEEKLY'
        return _FUNCTION_KEY, "Time Series FX (Weekly)", 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_monthly(self, from_symbol, to_symbol, outputsize='compact'):
        """ Returns the monthly exchange rate for any pair of physical
        currency (e.g., EUR) or physical currency (e.g., USD).

        Keyword Arguments:
            from_symbol: The currency you would like to get the exchange rate
                for.
                For example: from_symbol=EUR or from_symbol=USD.
            to_symbol: The destination currency for the exchange rate.
                For example: to_symbol=USD or to_symbol=JPY.
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min'
                (default '15min')
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length monthly times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = 'FX_MONTHLY'
        return _FUNCTION_KEY, "Time Series FX (Monthly)", 'Meta Data'
