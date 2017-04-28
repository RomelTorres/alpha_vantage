try:
    # Python 3 import
    from urllib.request import urlopen
except ImportError:
    # Python 2.* import
    from urllib2 import urlopen

from simplejson import loads

class AlphaVantage:
    """
        This class is in charge of creating a python interface between the Alpha
        Vantage restful API and your python application
    """
    _ALPHA_VANTAGE_API_URL = "http://www.alphavantage.co/query?"

    def __init__(self, key=None):
        self.key = key

    def _data_request(self, url):
        """ Request data from the given url and return it as a json
        object. It raises URLError

        Keyword arguments:
        url -- The url of the service
        """
        response = urlopen(url)
        url_response = response.read()
        json_response = loads(url_response)
        return json_response

    def get_intraday(self, symbol, interval='15min', outputsize='compact'):
        """ Return intraday time series in two json objects as data and
        meta_data. It raises ValueError when problem arise


        Keyword arguments:
        symbol -- the symbol for the equity we want to get its data
        interval -- time interval between two conscutive values,
        supported values are '1min', '5min', '15min', '30min', '60min'
        (default '15min')
        outputsize -- The size of the call, supported values are
        'compact' and 'full; the first returns the last 100 points in the
        data series, and 'full' returns the full-length intraday times
        series, commonly above 1MB (default 'compact')
        """
        _INTRADAY = "TIME_SERIES_INTRADAY"
        url = "{}function={}&symbol={}&interval={}&outputsize={}&apikey={}\
        ".format(AlphaVantage._ALPHA_VANTAGE_API_URL, _INTRADAY,  symbol,
        interval, outputsize, self.key)
        json_response = self._data_request(url)
        if 'Error Message' in json_response:
            raise ValueError('ERROR getting data form api',
            json_response['Error Message'])
        data = json_response['Time Series ({})'.format(interval)]
        meta_data = json_response['Meta Data']
        return data, meta_data
        
if __name__ == '__main__':
    av = AlphaVantage(key='486U')
    data, meta_data = av.get_intraday()
    print(data)
