.. alpha_vantage documentation master file, created by
   sphinx-quickstart on Sun May 28 14:23:31 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to alpha_vantage's documentation!
=========================================

|Build Status| |PyPI version| |Documentation Status|

*Python module to get stock data from the Alpha Vantage API*

The `Alpha Vantage Stock API <https://www.alphavantage.co/>`_ provides free JSON access to the stock market, plus a comprehensive set of technical indicators. This project is a python wrapper around this API to offer python plus json/pandas support. I hope you enjoy it.
It requires a free API, that can be requested on http://www.alphavantage.co/support/#api-key. This `stock API article <https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631>`_ also contains general guidance on ingesting and integrating with market data. 

If you are a spreadsheet user, see also: 
`Microsoft Excel Add-on <https://appsource.microsoft.com/en-us/product/office/WA200001365>`_ and
`Google Sheets Add-on <https://gsuite.google.com/marketplace/app/alpha_vantage_market_data/434809773372>`_ 

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

    from alpha_vantage.timeseries import TimeSeries
    import matplotlib.pyplot as plt

    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    data['close'].plot()
    plt.title('Intraday Times Series for the MSFT stock (1 min)')
    plt.show()


Code & Issue Tracker
====================
The code is hosted in github: https://github.com/RomelTorres/alpha_vantage
And the issue tracker as well: https://github.com/RomelTorres/alpha_vantage/issues

Contributions
=============
If you have a feature that you want to see merged in the code, please do a pull request with it and it will be evaluated.

Community Pulse
===============
* Alpha Vantage used by `Harvard COVID-19 Global Policy Tracker <https://projects.iq.harvard.edu/covidpt/global-policy-tracker>`_ (`link <https://www.hbs.edu/covid-19-business-impact/Insights/Economic-and-Financial-Impacts/Global-Policy-Tracker>`_) and `a recent economic review <http://blogs.harvard.edu/econreview/2020/08/25/why-you-need-a-reliable-stock-market-data-api-in-2020/>`_
* Alpha Vantage featured in `Xignite stock API press release <https://www.xignite.com/news/best-6-free-and-paid-stock-market-apis/>`_ and `Best 5 (Free and Paid) Stock Market APIs in 2020 <https://wp.nyu.edu/qids/2020/06/23/best-stock-api-2020/>`_ by NYU's Quantitative Investing project

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
.. |PyPI version| image:: https://badge.fury.io/py/alpha-vantage.svg
   :target: https://badge.fury.io/py/alpha_vantage
.. |Documentation Status| image:: https://readthedocs.org/projects/alpha-vantage/badge/?version=latest
   :target: http://alpha-vantage.readthedocs.io/en/latest/?badge=latest
