from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def make_noise(self) -> str: 
        pass

class Car(Vehicle):
    def make_noise(self):
        return "brm"


def f(vehicle: Vehicle):
    print(type(vehicle).__name__, '| noise: ', vehicle.make_noise())

# v = Vehicle() # make runtime error you cannot do this
c = Car()

f(c)

