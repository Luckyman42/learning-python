from typing import TypeVar, Generic
from animals import Animal, Dog

# T_contra is a contravariant type variable.
T_contra = TypeVar("T_contra", contravariant=True)

class Box(Generic[T_contra]):
    def __init__(self, value: T_contra):
        self.value = value

# This means: Box is *contravariant* in T.
# A contravariant type may only be used in input positions (write-only),
# and must NOT be used as output.

dog = Dog()
box_of_dog: Box[Dog] = Box(dog)

def get_animal_from_box(box: Box[Animal]) -> Animal:
    return box.value

# This is NOT allowed:
# Dog <: Animal, but for contravariant types we reverse the direction:
#    Box[Animal] <: Box[Dog]
# So Box[Dog] cannot be passed where Box[Animal] is expected.
#
# Static type checkers will flag this as an error:
get_animal_from_box(box_of_dog)   # ERROR – Box is contravariant

# But this will be OK
animal = Animal()
box_of_animal: Box[Animal] = Box(animal)
def get_dog_from_box(box: Box[Dog]) -> Dog:
    return box.value

get_dog_from_box(box_of_animal) # We can use Animal Box here



class WrongBox(Generic[T_contra]):
    def __init__(self, value: T_contra):
        self.value = value
    # Error (conceptually): a contravariant type variable cannot appear in output position
    def get_value(self) -> T_contra:
        return self.value
