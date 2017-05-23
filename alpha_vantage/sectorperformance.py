#!/usr/bin/env python
from .alphavantage import AlphaVantage as av
from functools import wraps
import pandas
import re

class SectorPerformances(av):
    """This class implements all the sector performance api calls
    """

    def percentage_to_float(self, val):
        """ Transform a string of ther form f.f% into f.f/100

        Keyword arguments:
        val -- The string to convert
        """
        return float(val.strip('%'))/100


    def _output_format_sector(func, override=None):
        """ Decorator in charge of giving the output its right format, either
        json or pandas (replacing the % for usable floats, range 0-1.0)

        Keyword arguments:
        func -- The function to be decorated
        override -- Override the internal format of the call, default None
        """
        @wraps(func)
        def _format_wrapper(self, *args, **kwargs):
            json_response, data_key, meta_data_key = func(self, *args, **kwargs)
            if isinstance(data_key, list):
                # Replace the strings into percentage
                data = {key: {k:self.percentage_to_float(v)
                for k,v in json_response[key].items()} for key in data_key}
            else:
                data = json_response[data_key]
            #TODO: Fix orientation in a better way
            meta_data = json_response[meta_data_key]
            # Allow to override the output parameter in the call
            if override is None:
                output_format = self.output_format.lower()
            elif 'json' or 'pandas' in override.lower():
                output_format = override.lower()
            # Choose output format
            if output_format == 'json':
                return data, meta_data
            elif output_format == 'pandas':
                data_pandas = pandas.DataFrame.from_dict(data,
                                                         orient='columns')
                # Rename columns to have a nicer name
                col_names = [re.sub(r'\d+.', '', name).strip(' ')
                             for name in list(data_pandas)]
                data_pandas.columns = col_names
                return data_pandas, meta_data
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.output_format))
        return _format_wrapper



    @_output_format_sector
    @av._call_api_on_func
    def get_sector(self):
        _FUNCTION_KEY = "SECTOR"
        # The keys for the json output
        _DATA_KEYS = ["Rank A: Real-Time Performance",
        "Rank B: 1 Day Performance",
        "Rank C: 5 Day Performance",
        "Rank D: 1 Month Performance",
        "Rank E: 3 Month Performance",
        "Rank F: Year-to-Date (YTD) Performance",
        "Rank G: 1 Year Performance",
        "Rank H: 3 Year Performance",
        "Rank I: 5 Year Performance",
        "Rank J: 10 Year Performance"]
        return _FUNCTION_KEY, _DATA_KEYS, 'Meta Data'
