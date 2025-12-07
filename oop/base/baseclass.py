class Vehicle():
    def make_noise(self) -> str: 
        return ""

class Car(Vehicle):
    def make_noise(self):
        return "brm"

def f(vehicle: Vehicle):
    print(type(vehicle).__name__, '| noise: ', vehicle.make_noise())

v = Vehicle() # You can do this 
c = Car()

f(v)
f(c)

# Not recommend
# If you just make a forward declaration in the base and not implementing method 
# You just get something like ABC but this is wrong (the pyright will not alert it as error) 

class Vehicle2():
    def make_noise(self) -> str: ...

class Car2(Vehicle2):
    def make_noise(self):
        return "brm"

def g(vehicle: Vehicle2):
    print(type(vehicle).__name__, '| noise: ', vehicle.make_noise())

v2 = Vehicle2() # Here you can do this 
c2 = Car2()

g(v2) # here noise just None
g(c2)
