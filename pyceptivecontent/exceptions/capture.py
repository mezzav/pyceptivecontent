from pyceptivecontent.exceptions.base import PyceptiveContentException, exception_error_code

@exception_error_code("APPLICATION_PLAN_CONTEXT_FAIL_ERROR")
class ApplicationPlanContextFailedError(PyceptiveContentException):
    pass