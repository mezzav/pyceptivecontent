from pyceptivecontent.adapter import HTTPAdapter
from pyceptivecontent.utilities import Utilities
from pyceptivecontent.document import Document
from pyceptivecontent.user import User
from pyceptivecontent.doctype import DocumentType, DocumentTypeList
from typing import Optional

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

    
    Once :func:`connect` is invoked, various properties will be available to make api calls.
    """

    def __init__(self, baseUrl: str, username: str, password: str):
        self.__auth = HTTPAdapter(baseUrl, username, password)

        self._buildVersion = None
        self._buildInterface = None
        self.__utilities = None
        self.__document = None

    @property
    def isConnected(self) -> bool:
        """
        Denotes if :class:`PyceptiveContent` is connected 
        to the Integration Server
        """
        return self.__auth.connected
    @property
    def buildVersion(self) -> str:
        """Intergration Server build version"""
        return self._buildVersion
    
    @property
    def buildInterface(self) -> str:
        """Integration Server build interface"""
        return self._buildInterface
        
    @property
    def utilities(self) -> Optional[Utilities]:
        """
        An class primirally used to assist in other functions
        such as calling an iScript, getting server status, etc. 
        """
        return self.__utilities
    
    @property
    def document(self) -> Optional[Document]:
        """A class that allows for document manipulation"""
        return self.__document 
    
    @property
    def user(self) -> Optional[User]:
        "A class that allows for user information retrieval"
        return self.__user

    @property
    def doctype(self) -> Optional[DocumentType]:
        "A class that retrieves document type information from Perceptive Content"
        return self.__doctype
    
    @property 
    def doctypelist(self) -> Optional[DocumentTypeList]:
        "A class that retrieves document type list information from Perceptive Content"
        return self.__doctypelist

    def connect(self) -> None:
        """
        Connects to the Integration Server and retrieves a session token for future calls. 
        """
        self.__auth.connect()

        self.__utilities = Utilities(self.__auth)
        serverData = self.utilities.serverVersion()
        
        self._buildVersion = serverData["buildVersion"]
        self._buildInterface = serverData["interfaceVersion"]


        self.__document = Document(self.__auth)
        self.__user = User(self.__auth)
        self.__doctype = DocumentType(self.__auth)
        self.__doctypelist = DocumentTypeList(self.__auth)


    def disconnect(self) -> None:
        """
        Disconnects to the Integration Server. 
        """
        self.__auth.disconnect()        

    def __enter__(self):
        self.connect()

        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.disconnect()
