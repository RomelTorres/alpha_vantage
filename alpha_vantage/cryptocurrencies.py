from .alphavantage import AlphaVantage as av


class CryptoCurrencies(av):
    """This class implements all the crypto currencies api calls
    """
    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_intraday(self, symbol, market):
        """ Returns the intraday (with 5-minute intervals) time series for a
        digital currency (e.g., BTC) traded on a specific market
        (e.g., CNY/Chinese Yuan), updated realtime. Prices and volumes are
        quoted in both the market-specific currency and USD.

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
            market: The exchange market of your choice. It can be any of the
            market in the market list. For example: market=CNY.
        """
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_INTRADAY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Intraday)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_daily(self, symbol, market):
        """ Returns  the daily historical time series for a digital currency
        (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan),
        refreshed daily at midnight (UTC). Prices and volumes are quoted in
        both the market-specific currency and USD..

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
            market: The exchange market of your choice. It can be any of the
            market in the market list. For example: market=CNY.
        """
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_DAILY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_weekly(self, symbol, market):
        """ Returns  the weekly historical time series for a digital currency
        (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan),
        refreshed daily at midnight (UTC). Prices and volumes are quoted in
        both the market-specific currency and USD..

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
            market: The exchange market of your choice. It can be any of the
            market in the market list. For example: market=CNY.
        """
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_WEEKLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Weekly)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_monthly(self, symbol, market):
        """ Returns  the monthly historical time series for a digital currency
        (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan),
        refreshed daily at midnight (UTC). Prices and volumes are quoted in
        both the market-specific currency and USD..

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
            market: The exchange market of your choice. It can be any of the
            market in the market list. For example: market=CNY.
        """
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_MONTHLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Monthly)', 'Meta Data'
