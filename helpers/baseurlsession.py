from urllib.parse import urljoin

import requests
from requests.models import Response


class BaseURLSession(requests.Session):
    """Subclassed version of requests.Session supporting a base URL to be used.
    
    Inspired by https://github.com/psf/requests/issues/2554#issuecomment-109341010
    """
    
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base = base_url
    
    def request(self, method, url, *args, **kwargs) -> Response:
        url = urljoin(self.base, url)
        return super(BaseURLSession, self).request(method, url, *args, **kwargs)
