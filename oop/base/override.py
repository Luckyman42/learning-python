from abc import ABC, abstractmethod
from typing import Protocol

# In python each class definition makes an instance of a type
# And if you inherite classes from each other there is the mro 
#   -> Method Resolution Order works as by the order of the declaration
# So the override works here, get searching for the specific method in the mro
# The first one is finded it will be what looking for

class Base:
    def f(self) -> str:
        return "Base"

class Derived(Base):
    def f(self) -> str:
        return "Derived"

print("Derived(Base): ", Derived().f(), " | mro: ", Derived.mro())

class AbstractBase(ABC):
    @abstractmethod
    def f(self) -> str:
        pass

class DA(ABC):
    def f(self) -> str:
        return "Derived from abstract"

print("DA(ABC): ", DA().f(), " | mro: ", DA.mro())

class BaseProtocol(Protocol):
    def f(self) -> str: ...
    
class DP(BaseProtocol):
    def f(self) -> str:
        return "Derived from abstract"

print("DP(BaseProtocol): ", DP().f(), " | mro: ", DP.mro())


class A:
    v : str = "a"
    def f(self) -> str:
        return "A"

class B:
    v : str = "a"
    def f(self) -> str:
        return "B"
    

class AB(A,B):
    pass
class BA(B,A):
    pass

ab = AB()
ba = BA()

print("AB: ", ab.f(),ab.v, " | mro: ", AB.mro())
print("BA: ", ba.f(),ba.v, " | mro: ", BA.mro())

