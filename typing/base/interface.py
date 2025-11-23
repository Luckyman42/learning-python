from typing import Protocol

class Vehicle(Protocol):
    def make_noise(self) -> str: ...

class Car(Vehicle):
    def make_noise(self):
        return "brm"

def g(vehicle: Vehicle):
    print(type(vehicle).__name__, '| noise: ', vehicle.make_noise())

# v = Vehicle() # You cannot do this it will be runtime error
c = Car()
