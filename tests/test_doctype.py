
from pyceptivecontent.models.doctype import DocumentTypeInfoModel, DocumentTypeModel, DocumentTypeListModel, DocumentTypeListInfoModel
from pyceptivecontent.exceptions.doctype import DocumentTypeNotFoundError, DocumentTypeListNotFoundError
import vcr
import os
import pytest

class TestDocumentType:
    # Set up default cassette options
    vcr_doctype = vcr.VCR(
        cassette_library_dir='tests/cassettes/doctype',
        serializer='json'
    )

    @vcr_doctype.use_cassette('doctypes_all.json')
    def test_get_all_doctype(self, documenttypes):
        
        assert isinstance(documenttypes, list)
        assert len(documenttypes) != 0

    @vcr_doctype.use_cassette('doctype_info.json')
    def test_get_doctype_info(self, pyceptivecontent_session, documenttypes):
        
        docTypeInfo = pyceptivecontent_session.doctype.info(type = documenttypes[0])

        assert isinstance(docTypeInfo, DocumentTypeInfoModel)

    @vcr_doctype.use_cassette('doctype_invalid.json')
    def test_get_invalid_doctype_info(self, pyceptivecontent_session):
        doctype = DocumentTypeModel(id = "3Z12SZAJ_ARJA9UF09UFHAFJOIA", name = "Invalid Document", description = "")

        with pytest.raises(DocumentTypeNotFoundError):
            pyceptivecontent_session.doctype.info(type = doctype)

class TestDocumentTypeList:
    # Set up default cassette options
    vcr_doctypelist = vcr.VCR(
        cassette_library_dir='tests/cassettes/doctypelist',
        serializer='json'
    )

    @vcr_doctypelist.use_cassette('doctypeslist_all.json')
    def test_get_all_doctypelists(self, documentypelists):
        
        assert isinstance(documentypelists, list)
        assert len(documentypelists) != 0

    @vcr_doctypelist.use_cassette('doctypelist_info.json')
    def test_get_doctypelist_info(self, pyceptivecontent_session, documentypelists):
        
        print(documentypelists[0])

        docTypeListInfo = pyceptivecontent_session.doctypelist.info(list = documentypelists[0])

        assert isinstance(docTypeListInfo, DocumentTypeListInfoModel)

    @vcr_doctypelist.use_cassette('doctypelist_invalid.json')
    def test_get_invalid_doctypelist_info(self, pyceptivecontent_session):
        doctype = DocumentTypeListModel(id = "3Z12SZAJ_ARJA9UF09UFHAFJOIA", name = "Invalid Document List", description = "")

        with pytest.raises(DocumentTypeListNotFoundError):
            pyceptivecontent_session.doctypelist.info(list = doctype)
    

