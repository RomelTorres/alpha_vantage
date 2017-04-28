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

    def __init__(self, key=None):
        self.key = key

    def _data_request(self):
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey={}".format(self.key)
        response = urlopen(url)
        json_response = loads(response.read())
        print(json_response)

if __name__ == '__main__':
    av = AlphaVantage(key='486U')
    av._data_request()
