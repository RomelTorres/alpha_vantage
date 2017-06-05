#!/usr/bin/env python
from .alphavantage import AlphaVantage as av
from functools import wraps
import re

class GlobalStockQuotes(av):
    """
        Implement the cllas to the Global Stock quotes from the alphavantage api.
        It can get, the following securities
            * Australian Securities Exchange: ASX
            * Bombay Stock Exchange: BOM
            * Borsa Italiana Milan Stock Exchange: BIT
            * Canadian/Toronto Securities Exchange: TSE
            * Deutsche Boerse Frankfurt Stock Exchange: FRA or ETR
            * Euronext Amsterdam: AMS
            * Euronext Brussels: EBR
            * Euronext Lisbon: ELI
            * Euronext Paris: EPA
            * London Stock Exchange: LON
            * Moscow Exchange: MCX
            * NASDAQ Exchange: NASDAQ
            * NASDAQ OMX Copenhagen: CPH
            * NASDAQ OMX Helsinki: HEL
            * NASDAQ OMX Iceland: ICE
            * NASDAQ OMX Stockholm: STO
            * National Stock Exchange of India: NSE
            * New York Stock Exchange: NYSE
            * Singapore Exchange: SGX
            * Shanghai Stock Exchange: SHA
            * Shenzhen Stock Exchange: SHE
            * Taiwan Stock Exchange: TPE
            * Tokyo Stock Exchange: TYO
    """

    @av._output_format
    @av._call_api_on_func
    def get_global_quote(self, symbol):
        """ This API returns the latest ticker information for securities
        traded at over 20 major exchanges in the world, updated realtime.

        Keyword Arguments:
            symbol: Symbols follow the format {exchangeName}:{symbolName}.
                For example: symbol=NASDAQ:MSFT. For US stocks only, the
                exchange name is optional: symbol=MSFT is equivalent to
                symbol=NASDAQ:MSFT.

        Returns:
            A dictionary containning the data from the api call, if the pandas
            format is selected, it will be overriden.
        """
        # Force the output format to be json when calling this function
        self.output_format = 'json'
        _FUNCTION_KEY = "GLOBAL_QUOTE"
        return _FUNCTION_KEY, "Realtime Global Securities Quote", None
