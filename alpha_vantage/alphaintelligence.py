from .alphavantage import AlphaVantage as av


class AlphaIntelligence(av):

    
    """This class implements all the api calls to alpha intelligence
    """
    @av._output_format
    @av._call_api_on_func
    def get_news_sentiment(self,tickers, topics=None, time_from=None, time_to=None,sort=None,limit=None):
        """live and historical market news & sentiment data from a large & growing selection of premier news 
        outlets around the world, covering stocks, cryptocurrencies, forex, and a wide range of topics such 
        as fiscal policy, mergers & acquisitions, IPOs, etc
        Visit alpha vantage documentation for details on keyboard arguments.
        Keyword Arguments:
            tickers: stock/crypto/forex symbols of your choice
            topics: news topics of your choice 
            time_from: time as UTC (ETC + 5 = UTC) as YYYYMMDDTHHMM
            time_to: time as UTC (ETC + 5 = UTC) as YYYYMMDDTHHMM
            sort: sort results based on EARLIEST, LATEST, RELEVANCE; default=Latest
            limit: number of matching results, default=50
        Returns: Pandas dataframe

        """
        _FUNCTION_KEY = "NEWS_SENTIMENT"
        return _FUNCTION_KEY, 'feed', None
    
    @av._output_format
    @av._call_api_on_func
    def get_top_gainers(self):
        """returns the top 20 gainers in the US market as pandas dataframe
        """
        _FUNCTION_KEY = "TOP_GAINERS_LOSERS"
        return _FUNCTION_KEY, 'top_gainers', None
    
    @av._output_format
    @av._call_api_on_func
    def get_top_losers(self):
        """returns the top 20 losers in the US market as pandas dataframe
        """
        _FUNCTION_KEY = "TOP_GAINERS_LOSERS"
        return _FUNCTION_KEY, 'top_losers', None
    
    
    @av._output_format
    @av._call_api_on_func
    def get_most_actively_traded(self):
        """returns the top 20 most active traded tickers in the US market as pandas dataframe
        """
        _FUNCTION_KEY = "TOP_GAINERS_LOSERS"
        return _FUNCTION_KEY, 'most_actively_traded', None