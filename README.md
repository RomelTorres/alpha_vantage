# alpha_vantage

[![Build Status](https://travis-ci.org/RomelTorres/alpha_vantage.png?branch=master)](https://travis-ci.org/RomelTorres/alpha_vantage)
[![PyPI version](https://badge.fury.io/py/alpha-vantage.svg)](https://badge.fury.io/py/alpha-vantage)
[![Documentation Status](https://readthedocs.org/projects/alpha-vantage/badge/?version=latest)](http://alpha-vantage.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Percentage of issues still open")

*Python module to get stock data/cryptocurrencies from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by [Alpha Vantage](https://www.alphavantage.co/). It requires a free API key, that can be requested from http://www.alphavantage.co/support/#api-key. You can have a look at all the API calls available in their [API documentation](https://www.alphavantage.co/documentation/).

For code-less access to financial market data, you may also consider [Wisesheets](https://www.wisesheets.io/) or the official [Google Sheet Add-on](https://gsuite.google.com/marketplace/app/alpha_vantage_market_data/434809773372) or the [Microsoft Excel Add-on](https://appsource.microsoft.com/en-us/product/office/WA200001365) by Alpha Vantage. Check out [this](https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631) guide for some common tips on working with financial market data. 

## News

* From version 2.3.0 onwards, fundamentals data and extended intraday is supported.
* From version 2.2.0 onwards, asyncio support now provided. See below for more information. 
* From version 2.1.3 onwards, [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage/) key integration is now available.
* From version 2.1.0 onwards, error logging of bad API calls has been made more apparent.
* From version 1.9.0 onwards, the urllib was substituted by pythons request library that is thread safe. If you have any error, post an issue.
* From version 1.8.0 onwards, the column names of the data frames have changed, they are now exactly what alphavantage gives back in their json response. You can see the examples in better detail in the following git repo:  https://github.com/RomelTorres/av_example
* From version 1.6.0, pandas was taken out as a hard dependency.

## Install
To install the package use:
```shell
pip install alpha_vantage
```
Or install with pandas support, simply install pandas too:
```shell
pip install alpha_vantage pandas
```

If you want to install from source, then use:
```shell
git clone https://github.com/RomelTorres/alpha_vantage.git
pip install -e alpha_vantage
```

## Usage
To get data from the API, simply import the library and call the object with your API key. Next, get ready for some awesome, free, realtime finance data. Your API key may also be stored in the environment variable ``ALPHAVANTAGE_API_KEY``.
```python
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
```
You may also get a key from [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage-alpha-vantage-default). Use your rapidAPI key for the key variable, and set ```rapidapi=True```

```python
ts = TimeSeries(key='YOUR_API_KEY',rapidapi=True)
```

Internally there is a retries counter, that can be used to minimize connection errors (in case that the API is not able to respond in time), the default is set to
5 but can be increased or decreased whenever needed.
```python
ts = TimeSeries(key='YOUR_API_KEY',retries='YOUR_RETRIES')
```
The library supports giving its results as json dictionaries (default), pandas dataframe (if installed) or csv, simply pass the parameter output_format='pandas' to change the format of the output for all the API calls in the given class. Please note that some API calls do not support the csv format (namely ```ForeignExchange, SectorPerformances and TechIndicators```) because the API endpoint does not support the format on their calls either.

```python
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas')
```

The pandas data frame given by the call, can have either a date string indexing or an integer indexing (by default the indexing is 'date'),
depending on your needs, you can use both.

```python
 # For the default date string index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='date')
# For the default integer index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='integer')
```

## Data frame structure
The data frame structure is given by the call on alpha vantage rest API. The column names of the data frames
are the ones given by their data structure. For example, the following call:
```python
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))
```
Would result on:
![alt text](images/docs_data_frame_header.png?raw=True "Data Header format.")

The headers from the data are specified from Alpha Vantage (in previous versions, the numbers in the headers were removed, but long term is better to have the data exactly as Alpha Vantage produces it.)
## Plotting
### Time Series
Using pandas support we can plot the intra-minute value for 'MSFT' stock quite easily:

```python
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

### Technical indicators
The same way we can get pandas to plot technical indicators like Bollinger Bands®

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

### Sector Performance
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

### Crypto currencies.

We can also plot crypto currencies prices like BTC:

```python
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()
```

Giving us as output:
![alt text](images/docs_cripto_btc.png?raw=True "Crypto Currenci daily (BTC)")

### Foreign Exchange (FX)

The foreign exchange endpoint has no metadata, thus only available as json format and pandas (using the 'csv' format will raise an Error)

```python
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='YOUR_API_KEY')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
pprint(data)
```
Giving us as output:
```
{
    '1. From_Currency Code': 'BTC',
    '2. From_Currency Name': 'Bitcoin',
    '3. To_Currency Code': 'USD',
    '4. To_Currency Name': 'United States Dollar',
    '5. Exchange Rate': '5566.80500105',
    '6. Last Refreshed': '2017-10-15 15:13:08',
    '7. Time Zone': 'UTC'
}
```

### Asyncio support

From version 2.2.0 on, asyncio support will now be available. This is only for python versions 3.5+. If you do not have 3.5+, the code will break.

The syntax is simple, just mark your methods with the `async` keyword, and use the `await` keyword. 

Here is an example of a for loop for getting multiple symbols asyncronously. This greatly improving the performance of a program with multiple API calls.

```python
import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


async def get_data(symbol):
    ts = TimeSeries(key='YOUR_KEY_HERE')
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data

loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()
print(results)
```

We have written a much more in depth article to explain asyncio for those who have never used it but want to learn about asyncio, concurrency, and multi-threading. Check it out here: [Which Should You Use: Asynchronous Programming or Multi-Threading?](https://medium.com/better-programming/which-should-you-use-asynchronous-programming-or-multi-threading-7435ec9adc8e?source=friends_link&sk=8c6c05c2bbc3666e9066547cb564c352)

## Examples

I have added a repository with examples in a python notebook to better see the
usage of the library: https://github.com/RomelTorres/av_example


## Tests

In order to run the tests you have to first export your API key so that the test can use it to run, also the tests require pandas, mock and nose.
```shell
export API_KEY=YOUR_API_KEY
cd alpha_vantage
nosetests
```

## Documentation
The code documentation can be found at https://alpha-vantage.readthedocs.io/en/latest/

## Contributing
Contributing is always welcome. Just contact us on how best you can contribute, add an issue, or make a PR. 

## TODOs:
* The integration tests are not being run at the moment within travis, gotta fix them to run.
* Add test for csv calls as well.
* Add tests for incompatible parameter raise errors.
* Github actions & other items in the issues page. 



## Contact:
You can reach/follow the Alpha Vantage team on any of the following platforms:
* [Slack](https://alphavantage.herokuapp.com/)
* [Twitter: @alpha_vantage](https://twitter.com/alpha_vantage)
* [Medium-Patrick](https://medium.com/@patrick.collins_58673)
* [Medium-AlphaVantage](https://medium.com/alpha-vantage)
* Email: support@alphavantage.co
* Community events: https://alphavhack.devpost.com/


## Star if you like it.
If you like or use this project, consider showing your support by starring it.

:venezuela:-:de:
