from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.exceptions.document import DocumentNotFoundError
from pyceptivecontent.models.document import DocumentModel, DocumentSignatureModel

from pyceptivecontent.endpoints import API_PATH

from typing import Dict, List, Union

from pathlib import Path
import os

class Document(PyceptiveContentBase):
    """
    A class that is responsible for retriving, updating, delete, and adding 
    documents to Perceptive Content
    """
    def __init__(self, auth):
        super().__init__(auth)

    @PyceptiveContentBase._required_args(params=["id"])
    def info(self, *argc, **kwargs) -> DocumentModel:
        """ 
        Retrieves information about a specific Perceptive Content document.

        :param id: document ID
        
        :raises DocumentNotFoundError: A document with :param:`id` does not exist in the system.
        :raises InsufficientPrivilegesError: User account authenticated with :class:`PyceptiveContent` does not have the privileges to view the document

        :return: Perceptive Content Document
        :rtype: DocumentModel
        """
        response, code, err = self._auth.request(
            method="GET", path=API_PATH["doc_info"].format(id=kwargs["id"])
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        return DocumentModel(
            **data,
            id = data["info"]['id'],
            name = data["info"]["name"],
            keys = data["info"]["keys"],
        )

    def signatures(self, document: DocumentModel, version: Union[str, int]) -> List[DocumentSignatureModel]:
        """
        Retrieves digital signatures associated with a document.

        :param document: Perceptive Content document model
        :param version: Denotes where to get all signatures, the latest signature, or signatures in a specific version of the document

        :returns: List of digital signatures
        :rtype: List[DocumentSignatureModel]
        """
        if not isinstance(version, str) and not isinstance(version, int):
            raise ValueError(
                "'version' parameter is not type 'str' or type 'int'")

        if isinstance(version, str) and version.upper() not in ["LATEST", "ALL"]:
            raise ValueError("'version' parameter is not 'LATEST', 'ALL'")

        query = { "version": version.upper() }

        response, code, err = self._auth.request(
            method="GET",
            path=API_PATH["doc_signatures"].format(id = document.id),
            params=query
        )

        if not response.ok:
            self.raiseException(code, err)
        
        return [
                DocumentSignatureModel(
                    **item, 
                    creationTime=item["creationInfo"]["createTime"], 
                    creationUsername= item["creationInfo"]["username"]
                ) 
                for item in response.json()["signatures"] 
            ]

    def export(self, doc: DocumentModel, path: str) -> None:
        """
            Exports a Perceptive Content document.

            :param doc: Perceptive Content document
            :param path: path to save the document.
        """
        params = {
            'documentId': doc.id,
            'conversionFormat': 'PDF'
        }    

        tempPath = Path(path)

        # create the directories if it does not exist
        if not os.path.exists(path):
            os.makedirs(tempPath.parent)

        auth = self._auth.copy(deep = True)

        auth.updateHeaders('Accept', 'application/zip')
    
        response = auth.request(
            method="GET", path=API_PATH["doc_export"], params=params)

        if not response.ok:
            pass

        with open(path, 'wb') as file:
            file.write(response.content)