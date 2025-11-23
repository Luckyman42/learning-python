from __future__ import annotations
from typing import Literal, LiteralString , TypeAlias, Protocol, Self

ID : TypeAlias = int
Color = Literal["black", "white", "orange"] 

class Cat(Protocol):
    id: ID
    color: Color
    def meow(self) -> LiteralString: ...
    def get_partner(self) -> Self|None: ...

def greet_cat(cat: Cat) -> None:
    print(f"Hello, {cat.color} cat with ID {cat.id}!")

class MyCat():
    id: ID
    color: Color 
    def __init__(self, id: ID, color: Color ):
        self.id = id
        self.color = color
    def meow(self) -> LiteralString:
        return "Meow!"

class AdultCat(MyCat):
    partner : Self | None = None  
    def set_partner(self, partner: Self) -> None:
        self.partner = partner
    def get_partner(self) -> Self | None :
        return self.partner

class OldCat(AdultCat):
    def meow(self) -> LiteralString:
        return "Meow... (softly)"

cat1 = MyCat(1, "black")
# greet_cat(cat1)
adult_cat = AdultCat(2, "orange")
old_cat = OldCat(2, "white")

adult_cat.set_partner(old_cat) # this will be ok because AdultCat::set_partner excepts AdultCat and OldCat <: AdultCat ->its OK by LSP
old_cat.set_partner(adult_cat) # this will be error because OldCat::set_partner excepts OldCat and OldCat <: AdultCat ->its not OK by LSP


