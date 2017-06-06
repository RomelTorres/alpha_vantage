.. alpha_vantage documentation master file, created by
   sphinx-quickstart on Sun May 28 14:23:31 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to alpha_vantage's documentation!
=========================================

|Build Status| |PyPI version| |Documentation Status|

*Python module to get stock data from the Alpha Vantage API*
Alpha Vantage http://www.alphavantage.co/ is a free JSON APIs for stock market
data, plus a comprehensive set of technical indicators. This project is a python wrapper
around this API to offer python plus json/pandas support. I hope you enjoy it.
It requires a free API, that can be
requested on http://www.alphavantage.co/support/#api-key.

Install
-------

To install the package use:

.. code:: shell

    pip install alpha_vantage

If you want to install from source, then use:

.. code:: shell

    git clone https://github.com/RomelTorres/alpha_vantage.git
    pip install -e alpha_vantage


Usage Example
=============
This is a simple code snippet to get global quotes from the

.. code:: python

    from alpha_vantage.globalstockquotes import GlobalStockQuotes
    from pprint import pprint
    gsq = GlobalStockQuotes(key='486U')
    data, meta_data = gsq.get_global_quote(symbol="ETR:DB1")
    pprint(data)

Return as output
::
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

Code & Issue Tracker
====================
The code is hosted in github: https://github.com/RomelTorres/alpha_vantage
And the issue tracker as well: https://github.com/RomelTorres/alpha_vantage/issues

Contributions
=============
If you have a feature that you want to see merged in the code, please do a pull
request with it and it will be evaluated.

License
=======
This project is licensed under the MIT license.

Contents
========
.. toctree::
    :maxdepth: 4


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Documentation
-------------

To find out more about the available api calls, visit the alpha-vantage
documentation at http://www.alphavantage.co/documentation/



.. |Build Status| image:: https://travis-ci.org/RomelTorres/alpha_vantage.png?branch=master
   :target: https://travis-ci.org/RomelTorres/alpha_vantage
.. |PyPI version| image:: https://badge.fury.io/py/alpha_vantage.svg
   :target: https://badge.fury.io/py/alpha_vantage
.. |Documentation Status| image:: https://readthedocs.org/projects/alpha-vantage/badge/?version=latest
   :target: http://alpha-vantage.readthedocs.io/en/latest/?badge=latest
