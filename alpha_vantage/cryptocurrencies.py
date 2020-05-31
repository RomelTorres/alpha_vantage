from .alphavantage import AlphaVantage as av


class CryptoCurrencies(av):
    """This class implements all the crypto currencies api calls
    """
    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments
        """
        super(CryptoCurrencies, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not compatible with the CryptoCurrencies class".format(
                self.output_format.lower()))
    
    @av._output_format
    @av._call_api_on_func
    def get_crypto_rating(self, symbol):
        """This API call returns the Crypto Rating for a chosen symbol
        
        Fundamental Crypto Asset Score (FCAS) is a comparative metric used 
        to assess the fundamental health of crypto projects. The score is derived 
        from the interactivity between primary project life-cycle factors: User 
        Activity/Utility, Developer Behavior, and Market Maturity. Each crypto 
        asset is given a composite numerical score, 0-1000
        
        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
        
        returns json or pandas only
        """
        _FUNCTION_KEY = 'CRYPTO_RATING'
        return _FUNCTION_KEY, 'Crypto Rating FCAS', None
    
    
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
    def get_digital_currency_exchange_rate(self, symbol, market):
        """ Returns the current exchange rate for a digital currency
        (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan),
        and when it was last updated.

        Keyword Arguments:
            symbol: The digital/crypto currency of your choice. It can be any
            of the currencies in the digital currency list. For example:
            symbol=BTC.
            market: The exchange market of your choice. It can be any of the
            market in the market list. For example: market=CNY.
        """
        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Dictonary (Digital Currency Exchange Rate)', 'Meta Data'
