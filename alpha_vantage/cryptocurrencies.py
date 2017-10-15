from .alphavantage import AlphaVantage as av


class CryptoCurrencies(av):
    """This class implements all the crypto currencies api calls
    """

    @av._call_api_on_func
    def get_currency_Exchange_rate(self, from_currency, to_currency):
        """ Returns the realtime exchange rate for any pair of digital
        currency (e.g., Bitcoin) or physical currency (e.g., USD).

        Keyword Arguments:
            from_currency: The currency you would like to get the exchange rate
            for. It can either be a physical currency or digital/crypto currency.
            For example: from_currency=USD or from_currency=BTC.
            to_currency: The destination currency for the exchange rate.
            It can either be a physical currency or digital/crypto currency.
             For example: to_currency=USD or to_currency=BTC.
            time_period:  How many data points to average (default 20)
            series_type:  The desired price type in the time series. Four types
                are supported: 'close', 'open', 'high', 'low' (default 'close')
        """
        _FUNCTION_KEY = "CURRENCY_EXCHANGE_RATE"
        return _FUNCTION_KEY, 'Technical Analysis: SMA', 'Meta Data'
