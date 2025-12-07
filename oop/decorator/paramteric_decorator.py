from functools import wraps
from typing import ParamSpec, TypeVar
from collections.abc import Callable

P = ParamSpec('P')
R = TypeVar('R')

def log(template : str):
    """ tempalte can contains: 
        - name
        - args
        - kwargs
        - result
        or the params in order {0}, {1} ...
    """
    def _log(func : Callable[P,R]) -> Callable[P,R]:
        @wraps(func)
        def wrapper(*args : P.args, **kwargs : P.kwargs):
            params : list[str] = [ i for i in func.__annotations__.keys() if i != 'return' ]
            args2 = [ kwargs.get(p) for p in params[len(args):] ]
            result = func(*args, **kwargs)
            print(template.format(*args, *args2, result=result, name=func.__name__, args=args ,kwargs=kwargs))
            return result
        return wrapper
    return _log

@log("{name}: ({0} + {1}) = {result}")
def s(a: int , b: int) -> int:
    return a+b

@log("{name} called!")
def b() -> int:
    return 42

s(2,b=1)
b()