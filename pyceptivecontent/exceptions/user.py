from pyceptivecontent.exceptions.base import PyceptiveContentException, exception_error_code

@exception_error_code("USER_NOT_FOUND_ERROR")
class UserNotFoundError(PyceptiveContentException):
    pass
