import pytest
from pyceptivecontent import PyceptiveContent
from dotenv import dotenv_values
import vcr
import os


@pytest.fixture(scope = "session")
def pyceptivecontent_session(request):
    config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

   
    pc = PyceptiveContent(config["SERVER_IP"], config["USERNAME"], config["PASSWORD"])

    pc.connect()

    #request.addfinalizer(lambda: pc.disconnect())    
   
    yield pc

    pc.disconnect()

@pytest.fixture(scope = "session")
def pyceptivecontent_session_minimal(request):
    config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

   
    pc = PyceptiveContent(config["SERVER_IP"], config["MINIMAL_ACCESS_USERNAME"], config["MINIMAL_ACCESS_PASSWORD"])

    pc.connect()

    #request.addfinalizer(lambda: pc.disconnect())    
   
    yield pc

    pc.disconnect()

@pytest.fixture(scope="session", autouse=True)
def valid_document(pyceptivecontent_session, pytestconfig):
    id = os.getenv("DOCUMENT_ID")

    doc = pyceptivecontent_session.document.info(id = id)

    # Yield or return the populated model
    yield doc