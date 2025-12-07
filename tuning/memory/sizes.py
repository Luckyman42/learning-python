import sys
from typing import Any
from collections.abc import Callable
from pympler import asizeof

n = None
i : int = 42
e : str = ""
c : str = "a"
hw : str = "Hello World"
b : bool = True
f : float = 3.14
d : dict[Any,Any] = {} 
l : list[Any] = []
s : set[Any] = set()
t: tuple[Any,...] = ()
la : Callable[[int],int] = lambda x : x
def fun():
    return None

print("Shellow size (sys.getsizeof) | real size (asizeof.asizeof)")
print("None: ", sys.getsizeof(n), asizeof.asizeof(n)) # type: ignore
print("int(42): ", sys.getsizeof(i), asizeof.asizeof(i)) # type: ignore
print("empty str: ", sys.getsizeof(e), asizeof.asizeof(e)) # type: ignore
print("str('a'): ", sys.getsizeof(c), asizeof.asizeof(c)) # type: ignore
print("str('Hello World'): ", sys.getsizeof(hw), asizeof.asizeof(hw)) # type: ignore
print("bool: ", sys.getsizeof(b), asizeof.asizeof(b)) # type: ignore
print("float(3.14): ", sys.getsizeof(f), asizeof.asizeof(f)) # type: ignore
print("empty dict : ", sys.getsizeof(d), asizeof.asizeof(d)) # type: ignore
print("empty list: ", sys.getsizeof(l), asizeof.asizeof(l)) # type: ignore
print("empty set: ", sys.getsizeof(s), asizeof.asizeof(s)) # type: ignore
print("empty tuple: ", sys.getsizeof(t), asizeof.asizeof(t)) # type: ignore
print("lambda int -> int: ", sys.getsizeof(la), asizeof.asizeof(la)) # type: ignore
print("function: ", sys.getsizeof(fun), asizeof.asizeof(fun)) # type: ignore
    