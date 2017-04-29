# alpha-vantage

[![Build Status](https://travis-ci.org/RomelTorres/alpha-vantage.png?branch=0.0.1)](https://travis-ci.org/RomelTorres/alpha-vantage)

*Python module to get stock data from the Alpha Vantage API*
Alpha Vantage delivers a free API for real time finantial data and most used finance indicators in a simple json format.

This module implements a python interface to the free API provided by Alpha
Vantage (http://www.alphavantage.co/). It requires a free API, that can be requested in their website.

## Install
```shell
git clone https://github.com/RomelTorres/alpha-vantage.git
cd alpha-vantage
python setup install
```

## Usage
To get data in a python, simply import the library and call the object with your api key and get ready for some awesome free realtime finance data.
```python
from alpha_vantage.alphavantage import AlphaVantage
av = AlphaVantage(key='YOUR_API_KEY')
data, meta_data = av.get_intraday('GOOGL')
```

## Next
More coming soon..
