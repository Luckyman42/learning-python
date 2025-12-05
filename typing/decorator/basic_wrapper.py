from typing import ParamSpec, TypeVar
from collections.abc import Callable

P = ParamSpec('P')
R = TypeVar('R')

print("START")

def decorator(fun : Callable[P,R]) -> Callable[P,R]:
    print("Decorator")
    def wrapper_fun(*args : P.args, **kwargs : P.kwargs):
        print("Wrapper start")
        result = fun(*args,**kwargs)
        print("Wrapper end")
        return result
    return wrapper_fun

print("Create a function with decorator")

@decorator
def up(word : str):
    wu = word.upper()
    print(wu)
    return wu

print("Call the function")
result = up("this is the function")
print("The result is: ", result)
