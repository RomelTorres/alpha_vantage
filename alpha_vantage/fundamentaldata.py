from .alphavantage import AlphaVantage as av

from datetime import datetime
search_date = datetime.now().date().strftime('%Y-%m-%d')

class FundamentalData(av):

    """This class implements all the api calls to fundamental data
    """
    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments.
        """
        super(FundamentalData, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not compatible with the FundamentalData class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_company_overview(self, symbol):
        """
        Returns the company information, financial ratios, 
        and other key metrics for the equity specified. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'OVERVIEW'
        return _FUNCTION_KEY, None, None

    @av._output_format
    @av._call_api_on_func
    def get_eps(self, symbol, interval=None):
        """
        Returns the Earnings per share (Eps) data for the company, either quarterly
        (including analyst estimates and earnings suprise) or annually or both.
        
        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval: what kind of eps data to return; 
                      annually [str]: return yearly eps as pandas dataframe
                      quarterly [str]: return quarterly eps as pandas dataframe
                      None [None]: return annual and quarterly data as a dict 
        """

        _FUNCTION_KEY = "EARNINGS"
        if interval == "quarterly":
            return _FUNCTION_KEY, "quarterlyEarnings", "symbol"
        elif interval == "annually":
            return _FUNCTION_KEY, "annualEarnings", "symbol"
        elif interval is None:
            return _FUNCTION_KEY, None, None
    
    @av._output_format
    @av._call_api_on_func
    def get_income_statement_annual(self, symbol):
        """
        Returns the annual and quarterly income statements for the company of interest. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'INCOME_STATEMENT'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_income_statement_quarterly(self, symbol):
        """
        Returns the annual and quarterly income statements for the company of interest. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'INCOME_STATEMENT'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_balance_sheet_annual(self, symbol):
        """
        Returns the annual and quarterly balance sheets for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'BALANCE_SHEET'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_balance_sheet_quarterly(self, symbol):
        """
        Returns the annual and quarterly balance sheets for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'BALANCE_SHEET'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_cash_flow_annual(self, symbol):
        """
        Returns the annual and quarterly cash flows for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'CASH_FLOW'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_cash_flow_quarterly(self, symbol):
        """
        Returns the annual and quarterly cash flows for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'CASH_FLOW'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'
