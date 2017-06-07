# alpha_vantage

[![Build Status](https://travis-ci.org/RomelTorres/alpha_vantage.png?branch=master)](https://travis-ci.org/RomelTorres/alpha_vantage)
[![PyPI version](https://badge.fury.io/py/alpha_vantage.svg)](https://badge.fury.io/py/alpha_vantage)
[![Documentation Status](https://readthedocs.org/projects/alpha-vantage/badge/?version=latest)](http://alpha-vantage.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Percentage of issues still open")

*Python module to get stock data from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by Alpha
Vantage (http://www.alphavantage.co/). It requires a free API, that can be requested on http://www.alphavantage.co/support/#api-key.

## Install
To install the package use:
```shell
pip install alpha_vantage
```

If you want to install from source, then use:
```shell
git clone https://github.com/RomelTorres/alpha_vantage.git
pip install -e alpha_vantage
```

## Usage
To get data in a python, simply import the library and call the object with your api key and get ready for some awesome free realtime finance data.
```python
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
```
Internally there is a retries counter, that can be used to minimize connection errors (in case that the api is not able to respond in time), the default is set to
5 but can be increased or decreased whenever needed.
```python
ts = TimesSeries(key='YOUR_API_KEY',retries='YOUR_RETRIES')
```
Finally the library supports giving its results as json dictionaries (default) or as pandas dataframe, simply pass the parameter output_format='pandas' to change
the format of the output for all the api calls.
```python
ts = TimesSeries(key='YOUR_API_KEY',output_format='pandas')
```

## Plotting
Using pandas support we can plot the intra-minute value for 'MSFT' stock quite easily:

```python
from alpha_vantage.timeseries import TimesSeries
import matplotlib.pyplot as plt

ts = TimesSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

The same way we can get pandas to plot technical indicators like Bolliger Bands®

```python
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ti_msft_example.png?raw=True "MSFT minute value plot example")

We can also plot sector performance just as easy:

```python
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()
```
Giving us as output:
![alt text](images/docs_sp_rt_example.png?raw=True "Real Time Sector Performance")

Finally if you want to get data from other stock exchange, you can do it as follows
(note that for this call only a dictionary will be returned, since it is not a times series):
```python
from alpha_vantage.globalstockquotes import GlobalStockQuotes
from pprint import pprint
gsq = GlobalStockQuotes(key='486U')
data, meta_data = gsq.get_global_quote(symbol="ETR:DB1")
pprint(data)
```
Giving as output
```python
{'01. Symbol': 'DB1',
 '02. Exchange Name': 'ETR',
 '03. Latest Price': '93.6100',
 '04. Open': '92.1400',
 '05. High': '93.6100',
 '06. Low': '91.9600',
 '07. Previous Close': '91.8300',
 '08. Price Change': '1.7800',
 '09. Price Change Percentage': '1.94%',
 '10. Volume (Current Trading Day)': '0.0',
 '11. 52-week Price Range': '64.50 - 94.58',
 '12. Market Cap': '18.07B',
 '13. PE Ratio': '21.76',
 '14. Last Updated': 'Jun 2, 5:35PM GMT+2'}
```

## Tests

In order to run the tests you have to first export your API key so that the test can use it to run.
```shell
export API_KEY=YOUR_API_KEY
cd alpha_vantage
nosetests
```

## Documentation
To find out more about the available api calls, visit the alpha-vantage documentation at http://www.alphavantage.co/documentation/ and to find out
about what this wrapper can do, please visit its own documentation at https://alpha-vantage.readthedocs.io/en/latest/
