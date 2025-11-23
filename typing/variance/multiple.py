from typing import Protocol, TypeVar, runtime_checkable

T= TypeVar('T') # invariant
T_cov = TypeVar('T_cov', covariant=True)
T_con = TypeVar('T_con', contravariant=True)

@runtime_checkable
class Getter(Protocol[T_cov]): # try to change this into T
    def get(self) -> T_cov: ...

@runtime_checkable
class Setter(Protocol[T_con]): # try to change this into T
    def set(self, value: T_con) -> None: ...

@runtime_checkable
class DataHandler(Getter[T], Setter[T], Protocol[T]): # Try to change here Getter/Setter type to T_cov, T_con
    pass

class MyData:
    def __init__(self, value: int) -> None:
        self._value = value

    def get(self) -> int:
        return self._value

    def set(self, value: int) -> None:
        self._value = value

def process_data(handler: DataHandler[int]) -> None:
    current_value = handler.get()
    print(f"Current value: {current_value}")
    handler.set(current_value + 10)
    print(f"New value set to: {handler.get()}")

data = MyData(5)
process_data(data)


def get_data[T](handler: Getter[T]) -> T:
    return handler.get()

get_data(data)  # Inferred type T is int

def set_data[T](handler: Setter[T], value: T) -> None:
    handler.set(value)

set_data(data, 42)  # Inferred type T is int