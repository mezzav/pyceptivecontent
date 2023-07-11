from abc import ABC, abstractmethod
from pyceptivecontent.exceptions.base import PyceptiveContentException
from pyceptivecontent.exceptions.document import *
from pyceptivecontent.exceptions.user import *
from pyceptivecontent.exceptions.doctype import *

class PyceptiveContentBase(ABC):
    def __init__(self, auth):
        self._auth = auth

    @abstractmethod
    def info(self, *argc, **kwargs):
        pass

    @classmethod
    def _required_args(cls, params: list):
        def decorator_func(func):
            def function_wrapper(self, *args, **kwargs):
                for param in params:
                    if param not in kwargs:
                        raise TypeError(f"Missing required parameter: {param}")
                return func(self, *args, **kwargs)
            return function_wrapper
        return decorator_func
    
    def raiseException(self, code, message):
        for exception_class in PyceptiveContentException.__subclasses__():
            if hasattr(exception_class, 'error_message') and exception_class.error_message in code:
                raise exception_class(message)
    
    
            