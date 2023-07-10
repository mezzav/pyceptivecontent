from pyceptivecontent.exceptions.document import DocumentNotFoundError
from pyceptivecontent.exceptions.base import InsufficientPrivilegesError
from pyceptivecontent.models.document import DocumentModel
import pytest
import os
import vcr
import secrets
import string
import zipfile

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(letters_and_digits) for _ in range(length))
    return random_string


class TestDocument:
    # Set up default cassette options
    vcr_document = vcr.VCR(
        cassette_library_dir='tests/cassettes/document',
        serializer='json'
    )

    @vcr_document.use_cassette('document_valid.json')
    def test_get_document(self, valid_document, pytestconfig):
        id = os.getenv("DOCUMENT_ID")
        
        assert valid_document.id == id

    @vcr_document.use_cassette("document_does_not_exist.json")
    def test_document_not_found(self, pyceptivecontent_session, pytestconfig):
        # document should not exist
        id = os.getenv("DOCUMENT_ID") + "ABCD09Z"

        with pytest.raises(DocumentNotFoundError):
            doc = pyceptivecontent_session.document.info(id = id)

    @vcr_document.use_cassette("document_no_access.json")
    def test_no_access_to_document(self, pyceptivecontent_session_minimal, pytestconfig):
        id = os.getenv("DOCUMENT_ID_NO_ACCESS")
        
        with pytest.raises(InsufficientPrivilegesError):
            doc = pyceptivecontent_session_minimal.document.info(id = id)

    @vcr_document.use_cassette("document_signatures.json")
    def test_get_signatures(self, pyceptivecontent_session, valid_document):
        id = os.getenv("DOCUMENT_ID")

        signatures = pyceptivecontent_session.document.signatures(valid_document, version = "ALL")

        assert len(signatures) == 0

    @vcr_document.use_cassette("export_document.yaml", serializer = "yaml")
    def test_export_valid_document(self, pyceptivecontent_session, valid_document, tmpdir):

        file_path = tmpdir.join("doc.zip")

        pyceptivecontent_session.document.export(valid_document, file_path)

        assert file_path.exists() == True
        