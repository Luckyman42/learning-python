from typing import overload

@overload
def func(x: int) -> int: ... # This just forward decl
@overload
def func(x: str) -> str: ...

def func(x : int | str) -> int | str:
    return x

# Here we knows that if the x is str -> the return will be str and not (int|str)


def i(i: int) -> None:
    pass
def s(s : str)-> None:
    pass

i(func(42))
s(func("42"))
i(func("42")) # this will be pyright error
s(func(42)) # this will be pyright error

# the function knows taht int -> int and str->str so it can calculate it
# even the func implementation returns with int|str 
# the pyright will understand that for int comes int so it allows you the i(func(42)) 
