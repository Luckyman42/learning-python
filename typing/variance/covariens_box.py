from typing import TypeVar, Generic
from animals import Animal, Dog

# T_co is a covariant type variable.
T_co = TypeVar("T_co", covariant=True)

class Box(Generic[T_co]):
    def __init__(self, value: T_co):
        self.value = value

    def get_value(self) -> T_co:   # allowed: covariant type used in output position
        return self.value

# This means: Box is covariant in T.
# A covariant type may only be *read* (output), not written (input).

dog = Dog()
box_of_dog: Box[Dog] = Box(dog)

def get_animal_from_box(box: Box[Animal]) -> Animal:
    return box.value

# This is allowed because Box is covariant:
# Dog <: Animal  ⇒  Box[Dog] <: Box[Animal]
get_animal_from_box(box_of_dog)

# If Box were invariant (like Python's built-in list), this would not work.


class WrongBox(Generic[T_co]):
    def __init__(self, value: T_co):
        self.value = value

    def set_value(self, val: T_co) -> None:
        # Error (conceptually): a covariant type variable cannot be used in input positions.
        self.value = val
