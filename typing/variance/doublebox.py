from typing import TypeVar, Generic
from animals import Animal, Dog, GermanShepherd

# Type variables
T_co = TypeVar("T_co", covariant=True)        # covariant: can be used in output (readonly)
T_contra = TypeVar("T_contra", contravariant=True)  # contravariant: can be used in input (writeonly)

class DoubleBox(Generic[T_co, T_contra]):
    # T_co is intended to be read-only (appears in outputs/returns)
    # T_contra is intended to be write-only (appears in inputs/parameters)
    def __init__(self, readonly_val: T_co, writeonly_val: T_contra):
        self.readonly_val = readonly_val    # T_co: only read from this slot (conceptually)
        self.writeonly_val = writeonly_val  # T_contra: only written to this slot (conceptually)

    def get_readonly(self) -> T_co:         # OK: covariant type used as return type
        return self.readonly_val

    def set_writeonly(self, val: T_contra) -> None:  # OK: contravariant type used as parameter
        self.writeonly_val = val


# Example objects
dog: Dog = Dog()
german_dog: GermanShepherd = GermanShepherd()
animal: Animal = Animal()


# Simple function that expects DoubleBox[Animal, Dog]
def f(box: DoubleBox[Animal, Dog]) -> None:
    pass


# Which DoubleBox instantiations can we pass to f(...) ?

f(DoubleBox[Animal, Dog](animal, dog))                 # exact match — OK

# Because of covariance on the first type parameter (T_co),
# and contravariance on the second (T_contra), these also work:
f(DoubleBox[Dog, Dog](dog, dog))                       # OK: Dog <: Animal for readonly slot
f(DoubleBox[GermanShepherd, Dog](german_dog, dog))     # OK: GermanShepherd <: Dog <: Animal


# But this does NOT work:
f(DoubleBox[Animal, GermanShepherd](animal, german_dog))   # Error: GermanShepherd is *not* acceptable for the write-only slot

# Conversely, replacing the write slot by a supertype is allowed:
f(DoubleBox[Animal, Animal](animal, animal))   # OK
f(DoubleBox[Dog, Animal](dog, animal))         # OK — first slot (readonly) Dog <: Animal, second slot (write) Animal is supertype of Dog


# Important conceptual relationship:
# Dog <: Animal
# Therefore, conceptually:
# DoubleBox[Dog, Animal]  <:  DoubleBox[Animal, Dog]
# (first parameter covariant: Dog -> Animal, second contravariant: Animal -> Dog)

# Static typing gotcha in Python (practical note):
# Even though the above subtype relation holds conceptually (because we declared variance),
# some patterns of instantiation/assignment can still be disallowed or flagged by type checkers
# if you mix raw constructors without explicit type parameters.

# Example that may be surprising at runtime vs. static-check time:
animal_and_dog: DoubleBox[Animal, Dog] = DoubleBox(Dog(), Animal())
# The line above uses the constructor without explicit generics and may fail static checks
# because the constructor call `DoubleBox(Dog(), Animal())` infers different type arguments.

# Safer two-step approach showing intended types:
dog_and_animal: DoubleBox[Dog, Animal] = DoubleBox(Dog(), Animal())
# Now the assignment using declared types is valid (as the declared relation holds):
animal_and_dog2: DoubleBox[Animal, Dog] = dog_and_animal
