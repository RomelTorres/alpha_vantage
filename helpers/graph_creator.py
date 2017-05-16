import os
from alpha_vantage.timeseries import TimesSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

if __name__ == '__main__':
    """
        Simple script to create the reference pictures
    """
    ts = TimesSeries(key=os.environ['API_KEY'], output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    data['close'].plot()
    plt.savefig('../images/docs_ts_msft_example.png')

    ti = TechIndicators(key=os.environ['API_KEY'], output_format='pandas')
    data, meta_data = ti.get_bbands(symbol='MSFT', interval='1min')
    plt.savefig('../images/docs_ti_msft_example.png')
