from typing import ParamSpec, TypeVar
from collections.abc import Callable
import time

P = ParamSpec('P')
R = TypeVar('R')

def mes_time(fun : Callable[P,R]) -> Callable[P,R]:
    def wrapper_fun(*args : P.args, **kwargs : P.kwargs):
        start = time.perf_counter()
        result = fun(*args,**kwargs)
        end = time.perf_counter()
        diff = end - start
        print(f"{fun.__name__}: {diff:.6f} sec")
        return result
    return wrapper_fun

@mes_time
def sum_inloop(li: list[int]) -> int:
    s : int = 0
    for i in li:
        s += i
    return s

@mes_time
def sum_fn(li : list[int]) -> int:
    return sum(li)


import random

l = [ random.randint(1000,100_000_000) for _ in range(1_000_000) ]

sum_inloop(l)
sum_fn(l)
