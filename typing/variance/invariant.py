from animals import Animal, Dog, Cat

def feed(animal: Animal) -> None:
    pass

def feed_all(animals: list[Animal]) -> None:
    pass

feed(Dog()) # This OK! because Dog is an Animal
feed_all([Dog(),Dog()]) # But this... is Wrong,  The lists are invariants!

# If list[Dog] <: list[Animal] then this should working:
dogs : list[Dog] = [Dog(), Dog()]

def add_cat(zoo: list[Animal]) -> None:
    zoo.append(Cat())

add_cat(dogs)  # This is an ERROR. Because the cat can be in danger.

# The tuple type is covariant becuase its inmutable:
def switch_animals(pair: tuple[Animal, Animal]) -> tuple[Animal, Animal]:
    # k : Animal = pair[0]
    # pair[0] = pair[1]  # This is not working you can't set a tuple
    # pair[1] = k
    # return pair
    return (pair[1], pair[0])

dog_cat_pair: tuple[Dog, Cat] = (Dog(), Cat())
switched_pair = switch_animals(dog_cat_pair)  # This is OK! 
# Because the original dog_cat_pair doesn't change, its a whole new tuple 
print(dog_cat_pair)
