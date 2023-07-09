from pyceptivecontent.adapter import HTTPAdapter
from pyceptivecontent.utilities import Utilities
from pyceptivecontent.document import Document

class PyceptiveContent:
    """ 
    A 'frontend' class used to interact with Perceptive Content Integration Server
    
    Instances of this class are the gateway to interactive with Perceptive Content's REST API.
    The canonical way to obtain an instance of this class is via:

    .. code-block:: python

        from pyceptivecontent import pyceptivecontent

        imagenow = PyceptiveContent("127.0.0.1:8080", "imagenow-test-account", "imagenow-test-password")
    
        # connects to the integration server
        imagenow.connect()

        # do Perceptive Content stuff here

        #disconnect from integration server
        imagenow.disconnect()
    """

    def __init__(self, baseUrl: str, username: str, password: str):
        self.__auth = HTTPAdapter(baseUrl, username, password)

        self._buildVersion = None
        self._buildInterface = None

    @property
    def buildVersion(self):
        return self._buildVersion
    
    @property
    def buildInterface(self):
        return self._buildInterface
        
    def connect(self):
        self.__auth.connect()

        self.utilities = Utilities(self.__auth)
        serverData = self.utilities.serverVersion()
        
        self._buildVersion = serverData["buildVersion"]
        self._buildInterface = serverData["interfaceVersion"]


        self.document = Document(self.__auth)


    def disconnect(self):
        self.__auth.disconnect()

    def __enter__(self):
        self.connect()

        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.disconnect()
