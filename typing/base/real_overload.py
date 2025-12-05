from singledispatch import
from multipledispatch import dispatch


@dispatch(int)
def fun(x : int):
    print("int: ", x)

@dispatch(str)
def fun(x : str):
    print("str: ", x)

@dispatch(int, str)
def fun(x : int, s : str):
    print("int, str: ", x, s)

@dispatch(int, int)
def fun(x : int, y: int):
    print("int, int: ", x, y)


fun(1)
fun("Hi")
fun(1,"hi")
fun(1,2)