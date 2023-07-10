from collections import namedtuple
from urllib.parse import urlunparse, urlparse
import requests

from pyceptivecontent.endpoints import API_PATH
from pyceptivecontent.exceptions.adapter import LoginFailedError, LogoutFailedError
from pyceptivecontent.utilities import multi_urljoin

urlComponent = namedtuple(
    typename="urlComponent",
    field_names=['scheme', 'netloc', 'url', 'path', 'query', 'fragment']
)

class HTTPAdapter:
    def __init__(self, baseUrl, username, password):
        self._url = urlparse(urlunparse(
            urlComponent(
                scheme="http",
                netloc=baseUrl,
                url="integrationserver/",
                query = "",
                path = "",
                fragment = ""
            )
        ))
        
        self._session = requests.Session()

        self._session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

        self._session.auth = requests.auth.HTTPBasicAuth(username, password)
        self.connected = False

    def request(self, method: str, path: str, **kwargs):
        url = self._url._replace(
            path = multi_urljoin(self._url.path, path)
        )


        try:
            response = self._session.request(
                method = method,
                url = urlunparse(url),
                params = kwargs.get("params"),
                json = kwargs.get("json"),
                data = kwargs.get("data"),
                files = kwargs.get("files")
            )
            
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(
                f"Error: {e.__dict__['response']} for {method} request on {urlunparse(url)}: {response.text}"
            )
        
        return response, response.headers.get("X-IntegrationServer-Error-Code"), response.headers.get('X-IntegrationServer-Error-Message')
    
    def connect(self):
        response, code, err = self.request(method = "GET", path = API_PATH["connect"])

        if not response.ok:
            raise LoginFailedError(err)
        
        self._session.headers.update({
            'X-IntegrationServer-Session-Hash': response.headers.get('X-IntegrationServer-Session-Hash')
        })

        self.connected = True
    
    def disconnect(self):
        response, code, err = self.request(method = "DELETE", path = API_PATH["disconnect"])

        if not response.ok:
            raise LogoutFailedError(
                f"{err}. Logout via Perceptive Content Mangement Console ('Cross Department Settings' -> 'Sessions')"
            )
        
        del self._session.headers["X-IntegrationServer-Session-Hash"]

        self.connected = False

    def updateHeaders(self, key, value):
        self._session.headers.update({
            key: value
        })