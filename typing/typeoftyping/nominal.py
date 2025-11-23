# Inheritance based typing

class Vehicle:
    wheel : int
    def __init__(self, wheel: int):
        self.wheel = wheel

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)

class Motor(Vehicle):
    def __init__(self):
        super().__init__(2)

def f(vehicle: Vehicle):
    print(type(vehicle).__name__, '| wheel count: ', vehicle.wheel)

v = Vehicle(0) # technically you can do this
c = Car()
m = Motor()

f(v)
f(c)
f(m)

# inheritance only from saying in the definition that you from "base"

class ShoppingCart():
    wheel : int = 4

sc = ShoppingCart()
f(sc) # It has wheel (so duck typing says ok) but not inherit Vehicle so it is cannot be replaced