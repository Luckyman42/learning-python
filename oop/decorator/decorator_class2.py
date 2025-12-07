from typing import ParamSpec, TypeVar, Any
import time

P = ParamSpec('P')
R = TypeVar('R')

class MesTime:
    def __init__ (self, func : Any):
        self._func = func
    
    def __call__(self, *args : Any, **kwargs : Any ):
        start = time.perf_counter()
        result = self._func(*args,**kwargs)
        end = time.perf_counter()
        diff = end - start
        print(f"{self._func.__name__}: {diff:.6f} sec")
        return result


@MesTime
def sum_inloop(li: list[int]) -> int:
    s : int = 0
    for i in li:
        s += i
    return s

@MesTime
def sum_fn(li : list[int]) -> int:
    return sum(li)

import random

l = [ random.randint(1000,100_000_000) for _ in range(1_000_000) ]

sum_inloop(l)
sum_fn(l)
