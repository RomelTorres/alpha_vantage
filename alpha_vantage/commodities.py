from .alphavantage import AlphaVantage as av


class Commodities(av):
    """This class implements all the commodities api calls
    """
    @av._output_format
    @av._call_api_on_func
    def get_wti(self, interval='monthly'):
        """ Returns the West Texas Intermediate (WTI) crude oil prices.

        Keyword Arguments:
            interval:  supported values are 'daily', 'weekly', 'monthly' (default 'monthly')
        """
        _FUNCTION_KEY = 'WTI'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_brent(self, interval='monthly'):
        """ Returns the Brent (Europe) crude oil prices.

        Keyword Arguments:
            interval:  supported values are 'daily', 'weekly', 'monthly' (default 'monthly')
        """
        _FUNCTION_KEY = 'BRENT'
        return _FUNCTION_KEY, 'data', None

    @av._output_format
    @av._call_api_on_func
    def get_natural_gas(self, interval='monthly'):
        """ Returns the Henry Hub natural gas spot prices.

        Keyword Arguments:
            interval:  supported values are 'daily', 'weekly', 'monthly' (default 'monthly')
        """
        _FUNCTION_KEY = 'NATURAL_GAS'
        return _FUNCTION_KEY, 'data', None

    @av._output_format
    @av._call_api_on_func
    def get_gold(self, interval='monthly', symbol='GOLD'):
        """ Returns historical prices for gold.

        Keyword Arguments:
            interval:  supported values are 'daily', 'weekly', 'monthly' (default 'monthly')
            symbol:  supported values are 'GOLD' and 'XAU' (default 'GOLD')
        """
        _FUNCTION_KEY = 'GOLD_SILVER_HISTORY'
        return _FUNCTION_KEY, 'data', 'nominal'

    @av._output_format
    @av._call_api_on_func
    def get_silver(self, interval='monthly', symbol='SILVER'):
        """ Returns historical prices for silver.

        Keyword Arguments:
            interval:  supported values are 'daily', 'weekly', 'monthly' (default 'monthly')
            symbol:  supported values are 'SILVER' and 'XAG' (default 'SILVER')
        """
        _FUNCTION_KEY = 'GOLD_SILVER_HISTORY'
        return _FUNCTION_KEY, 'data', 'nominal'

    @av._output_format
    @av._call_api_on_func
    def get_gold_spot(self, symbol='GOLD'):
        """ Returns the realtime spot price for gold.

        Keyword Arguments:
            symbol:  supported values are 'GOLD' and 'XAU' (default 'GOLD')
        """
        _FUNCTION_KEY = 'GOLD_SILVER_SPOT'
        return _FUNCTION_KEY, None, None

    @av._output_format
    @av._call_api_on_func
    def get_silver_spot(self, symbol='SILVER'):
        """ Returns the realtime spot price for silver.

        Keyword Arguments:
            symbol:  supported values are 'SILVER' and 'XAG' (default 'SILVER')
        """
        _FUNCTION_KEY = 'GOLD_SILVER_SPOT'
        return _FUNCTION_KEY, None, None

    @av._output_format
    @av._call_api_on_func
    def get_copper(self, interval='monthly'):
        """ Returns the global price of copper.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'COPPER'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_aluminum(self, interval='monthly'):
        """ Returns the global price of aluminum.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'ALUMINUM'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_wheat(self, interval='monthly'):
        """ Returns the global price of wheat.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'WHEAT'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_corn(self, interval='monthly'):
        """ Returns the global price of corn.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'CORN'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_cotton(self, interval='monthly'):
        """ Returns the global price of cotton.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'COTTON'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_sugar(self, interval='monthly'):
        """ Returns the global price of sugar.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'SUGAR'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_coffee(self, interval='monthly'):
        """ Returns the global price of coffee.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'COFFEE'
        return _FUNCTION_KEY, 'data', None
    
    @av._output_format
    @av._call_api_on_func
    def get_price_index(self, interval='monthly'):
        """ Returns the global price index of all commodities.

        Keyword Arguments:
            interval:  supported values are 'monthly', 'quarterly', 'annual' (default 'monthly')
        """
        _FUNCTION_KEY = 'ALL_COMMODITIES'
        return _FUNCTION_KEY, 'data', None