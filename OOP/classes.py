from typing import Union
from abc import abstractmethod, ABC

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    @property
    def fullname(self):
        return self.name
    @fullname.setter
    def fullname_set(self, val):
        self.name = val
# Nedarvning
class Staff(Person):
    # Constructor, returnere en instans af people
    def __init__(self, name:str, age:int, staff_id:int):
        # Kører constructor fra den nedarvede klasse,
        # Sender self som er instans af Staff klassen som Metoden senere returnere
        super().__init__(name, age)
        self.staff_id = staff_id

class People:
    def __init__(self, *people: Union[Person, Staff]):
        self.people = list(people)
    
    def add(self, *person: Union[Person, Staff]):
        for i in person:
            if not type(i) in [Person, Staff]:
                raise TypeError("Person must be object of Person or Staff class")
            self.people.append(i)

    __add__ = add

    def __iter__(self):
        for i in self.people:
            yield [i.name, i.age]

class AbstractPerson(ABC):
    @abstractmethod
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    @abstractmethod
    def __addToAge__():
        self.age += 1


""" Accesibility
Python har ikke Accesibility til deres klasser, 
Istedet har man lavet det standard practice at bruge dunder (__) får og efter metoder og properties som skal ses som private,
f.eks __add__, __name__

I C# er der en række forskellige, f.eks.
Private: Metoder og properties som kun kan tilgås fra metoder inde i dens egen klasse

Public: Det modsatte af private,
Metoder og properties som kan tilgås fra alle metoder

Protected: Metoder og properties der kun kan tilgås fra dens egen klasse eller en klasse som nedarver fra den.

Internal: Metoder og properties som kun kan tilgås fra den samme assembly.
"""