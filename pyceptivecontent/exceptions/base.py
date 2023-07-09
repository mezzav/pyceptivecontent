class PyceptiveContentException(Exception):
    pass

def exception_error_code(error_message):
    def decorator(exception_class):
        exception_class.error_message = error_message
        return exception_class
    return decorator


@exception_error_code("INSUFFICIENT_PRIVILEGES_ERROR")
class InsufficientPrivilegesError(PyceptiveContentException):
    pass

