#!/usr/bin/env python
from .alphavantage import AlphaVantage as av

class SectorPerformances(av):
    """This class implements all the sector performance api calls
    """
    @av._output_format
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
