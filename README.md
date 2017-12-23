# alpha_vantage

[![Build Status](https://travis-ci.org/RomelTorres/alpha_vantage.png?branch=master)](https://travis-ci.org/RomelTorres/alpha_vantage)
[![PyPI version](https://badge.fury.io/py/alpha_vantage.svg)](https://badge.fury.io/py/alpha_vantage)
[![Documentation Status](https://readthedocs.org/projects/alpha-vantage/badge/?version=latest)](http://alpha-vantage.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Percentage of issues still open")

*Python module to get stock data/cryptocurrencies from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by Alpha
Vantage (http://www.alphavantage.co/). It requires a free API, that can be requested on http://www.alphavantage.co/support/#api-key. You can have a look at all the api calls available in their documentation http://www.alphavantage.co/documentation

## Install
To install the package use:
```shell
pip install alpha_vantage
```
Since version 1.6.0 pandas was taken out as a hard dependency, so if you want to have pandas support install pandas too:
```shell
pip install alpha_vantage, pandas
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
ts = TimeSeries(key='YOUR_API_KEY',retries='YOUR_RETRIES')
```
Finally the library supports giving its results as json dictionaries (default), pandas dataframe (if installed) or csv, simply pass the parameter output_format='pandas' to change the format of the output for all the api calls in the given class. Please note that some API calls do not support the csv format (namely ```ForeignExchange, SectorPerformances and TechIndicators```) because the API endpoint does not support the format on their calls either.

```python
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas')
```

## Plotting
### Time Series
Using pandas support we can plot the intra-minute value for 'MSFT' stock quite easily:

```python
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

### Technical indicators
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
data, meta_data = cc.get_digital_currency_intraday(symbol='BTC', market='CNY')
data['. price (USD)'].plot()
plt.tight_layout()
plt.title('Intraday value for bitcoin (BTC)')
plt.grid()
plt.show()
```

Giving us as output:
![alt text](images/docs_cripto_btc.png?raw=True "Crypto Currenci daily (BTC)")

### Foreign Exchange (FX)

```python
cc = ForeignExchange(key=os.environ['API_KEY'])
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
print(data)
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
m}
```

## Examples

I have added a repository with examples in a python notebook to better see the
usage of the library: https://github.com/RomelTorres/av_example


## Tests

In order to run the tests you have to first export your API key so that the test can use it to run.
```shell
export API_KEY=YOUR_API_KEY
cd alpha_vantage
nosetests
```

## Documentation
The code documentation can be found at https://alpha-vantage.readthedocs.io/en/latest/

## Contributing
Contributing is always welcome, since sometimes I am busy. Just contact me on how est you can contribute.  

## Star if you like it.
If you like or use this project, consider showing your support by staring it.
From Venezuela with Love...
