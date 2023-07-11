from pyceptivecontent.exceptions.base import PyceptiveContentException, exception_error_code

@exception_error_code("DOCUMENT_TYPE_NOT_FOUND_ERROR")
class DocumentTypeNotFoundError(PyceptiveContentException):
    pass

@exception_error_code("DOCUMENT_TYPE_LIST_NOT_FOUND_ERROR")
class DocumentTypeListNotFoundError(PyceptiveContentException):
    pass