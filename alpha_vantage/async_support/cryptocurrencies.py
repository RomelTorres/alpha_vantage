from .alphavantage import AlphaVantage as av


class CryptoCurrencies(av):
    """This class implements all the crypto currencies api calls
    """
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

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_exchange_rate(self, from_currency, to_currency):
        """ Returns the realtime exchange rate for any pair of digital
        currency (e.g., BTC) or physical currency (e.g., USD).
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
    def get_digital_crypto_rating(self, symbol):
        """ Returns the Fundamental Crypto Asset Score for a digital currency
        (e.g., BTC), and when it was last updated.

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
        """
        _FUNCTION_KEY = 'CRYPTO_RATING'
        return _FUNCTION_KEY, 'Crypto Rating (FCAS)', None
