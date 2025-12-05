from collections.abc import Callable
from typing import Any

def Id(id:int) -> Callable[[type], type]:
    def class_decorator(cls: type):
        cls.id = id
        return cls
    return class_decorator


@Id(3)
class A:
    name: str
    def __init__(self, name: str):
        self.name = name

a = A("alma")
print(a.id)



def info(cls: type) -> type:
    def _print_info(self : Any):
        print(cls.__doc__)
    cls.info = _print_info
    return cls

@info
class Hello:
    """This class is for saying hello"""
    def say(self):
        print("Hello")

h = Hello()
h.info()