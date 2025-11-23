# Stucture based typing

class Car():
    wheel : int = 4

class Cat():
    def speak(self) -> str:
        return "meow"

def f(a):
    print(type(a).__name__, '| wheel count: ', a.wheel)

car = Car()
cat = Cat()
cat.wheel = 42 
f(car)
f(cat)

# in typing this is a disaster but in runtime this is totally fine, because of duck typing

