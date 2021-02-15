from typing import Optional, Mapping
from urllib.parse import urljoin

import aiohttp
from aiohttp import ClientResponse as ClientResponse
from aiohttp.typedefs import StrOrURL


class AsyncBaseURLSession(aiohttp.ClientSession):
    """Subclassed version of aiohttp.ClientSession supporting a base URL to be used."""
    
    def __init__(self, base_url: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.base = base_url
        self.params = {}
    
    async def _request(self, method: str, str_or_url: StrOrURL, *args,
                       params: Optional[Mapping[str, str]] = None, **kwargs) -> ClientResponse:
        # Join parameter dictionaries.
        joined_params = self.params.copy()
        for key in params:
            joined_params[key] = str(params[key])
        
        # Join base URL with specified URL.
        url = urljoin(self.base, str_or_url)
        
        return await super()._request(method, url, *args, params=joined_params, **kwargs)
