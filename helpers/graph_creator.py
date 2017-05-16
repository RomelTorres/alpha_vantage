import sys
import os
try:
    from alpha_vantage.api_calls.timeseries import TimesSeries
    from alpha_vantage.api_calls.techindicators import TechIndicators
except ImportError:
    # TODO: Remove this in the future (too ugly)
    sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
    from alpha_vantage.api_calls.timeseries import TimesSeries
    from alpha_vantage.api_calls.techindicators import TechIndicators


import matplotlib.pyplot as plt

if __name__ == '__main__':
    """
        Simple script to create the reference pictures
    """
    ts = TimesSeries(key=os.environ['API_KEY'], output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    data['close'].plot()
    plt.title('Intraday Times Series for the MSFT stock (1 min)')
    plt.grid()
    plt.show()

    ti = TechIndicators(key=os.environ['API_KEY'], output_format='pandas')
    data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
    data.plot()
    plt.title('BBbands indicator for  MSFT stock (60 min)')
    plt.grid()
    plt.show()
