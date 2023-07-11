from pyceptivecontent.base import PyceptiveContentBase
from pyceptivecontent.models.doctype import DocumentTypeInfoModel, DocumentTypeModel, DocumentTypeListInfoModel, DocumentTypeListModel

from pyceptivecontent.endpoints import API_PATH

import json

class DocumentType(PyceptiveContentBase):
    
    def __init__(self, auth):
        super().__init__(auth)

    def all(self):
        """
        Retrieves all document types from Perceptive Content

        :return: A list of document types
        :rtype: List[DocumentTypeModel]
        """
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["all_document_types"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        documentTypes = []
        for documentType in data["documentTypes"]:
            documentTypes.append(DocumentTypeModel(**documentType))

        return documentTypes


    @PyceptiveContentBase._required_args(params = ["type"])
    def info(self, *argc, **kwargs):
        """
        Retrieves information about a specific document type.

        :param type: The document type
        :returns: Detailed information about the document type
        :rtype: DocumentTypeInfoModel
        """
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["document_type_info"].format(id = kwargs["type"].id)
        )

        if not response.ok:
            self.raiseException(code, err)

        print(code)
        print()
        
        data = response.json()

        return DocumentTypeInfoModel(**data)
    
class DocumentTypeList(PyceptiveContentBase):
    
    def __init__(self, auth):
        super().__init__(auth)

    def all(self):
        """
        Retrieves all document types lists from Perceptive Content

        :return: A list of document types lists
        :rtype: List[DocumentTypeListModel]
        """

        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["all_document_type_lists"]
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        docTypeLists = []
        for docTypeList in data["documentTypeLists"]:
            docTypeLists.append(DocumentTypeListModel(**docTypeList))

        return docTypeLists

    @PyceptiveContentBase._required_args(params = ["list"])
    def info(self, *argc, **kwargs):
        """
        Retrieves all document types lists from Perceptive Content

        :return: Detailed information about the document type list
        :rtype: DocumentTypeListModel
        """
        response, code, err = self._auth.request(
            method = "GET", path = API_PATH["document_type_list_info"].format(id = kwargs["list"].id)
        )

        if not response.ok:
            self.raiseException(code, err)

        data = response.json()

        print(json.dumps(data, indent = 4))

        return DocumentTypeListInfoModel(**data)
    