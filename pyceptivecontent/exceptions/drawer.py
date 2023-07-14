from pyceptivecontent.exceptions.base import PyceptiveContentException, exception_error_code

@exception_error_code("DRAWER_NOT_FOUND_ERROR")
class DrawerNotFoundError(PyceptiveContentException):
    pass