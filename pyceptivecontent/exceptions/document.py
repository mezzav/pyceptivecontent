from pyceptivecontent.exceptions.base import PyceptiveContentException, exception_error_code

@exception_error_code("DOCUMENT_NOT_FOUND_ERROR")
class DocumentNotFoundError(PyceptiveContentException):
    pass
