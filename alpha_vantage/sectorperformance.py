#!/usr/bin/env python
from .alphavantage import AlphaVantage as av


class SectorPerformances(av):
    """This class implements all the sector performance api calls
    """

    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments
        """
        super(SectorPerformances, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not comatible with the SectorPerformances class".format(
                self.output_format.lower()))

    def percentage_to_float(self, val):
        """ Transform a string of the form f.f% into f.f/100

        Keyword Arguments:
            val: The string to convert
        """
        return float(val.strip('%')) / 100

    @av._output_format_sector
    @av._call_api_on_func
    def get_sector(self):
        """This API returns the realtime and historical sector performances
        calculated from S&P500 incumbents.

        Returns:
            A pandas or a dictionary with the results from the api call
        """
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
