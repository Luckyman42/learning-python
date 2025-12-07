from functools import wraps
from typing import ParamSpec, TypeVar
from collections.abc import Callable

P = ParamSpec('P')
R = TypeVar('R')

class CallCounter:
    def __init__(self):
        self.counter : dict[str,int] = {}    
    def count(self, func : Callable[P,R]) -> Callable[P,R]:
        self.counter[func.__name__] = 0
        @wraps(func)
        def wrapper(*args : P.args, **kwargs : P.kwargs):
            self.counter[func.__name__] += 1
            return func(*args, **kwargs)
        return wrapper

counter = CallCounter()

@counter.count
def a():
    return "a"

@counter.count
def b():
    return "b"


for i in range(10):
    a()
    if i % 2 == 0:
        b()

print(counter.counter)