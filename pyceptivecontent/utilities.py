from urllib.parse import urlunparse, urljoin, urlparse, urlencode, quote_plus

from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.endpoints import API_PATH

def multi_urljoin(* parts):
    return urljoin(parts[0], "/".join(quote_plus(part.strip("/"), safe = "/") for part in parts[1:]))

class Utilities(PyceptiveContentBase):
    def __init__(self, auth):
        super().__init__(auth)

    def info(self, *argc, **kwargs):
        pass

    def serverVersion(self):
        response, code, err = self._auth.request(method = "GET", path = API_PATH["server_version"])

        if not response.ok:
            pass

        return response.json()
    
    def serverStatus(self):
        response, code, err = self._auth.request(method = "GET", path = API_PATH["server_status"])

        if not response.ok:
            pass

        return response.json()

