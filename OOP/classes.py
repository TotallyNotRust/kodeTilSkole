from typing import Union
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
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

class AbstractPerson:
    def __add__():
        raise NotImplementedError
    def return_self():
        raise NotImplementedError

""" Overrides:
Python har ikke overrides da variabler ikke har en statisk type
I f.eks. C# ville man bruge overrides til at have en metode der kan tage både en int og en float
static int add(int one, int two) {
    return one + two;
}
static float add(float one, float two) {
    return one + two;
}
"""
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
""" Properties
Et variable der har en getter og setter.
De kan f.eks bruges til at vælge hvordan en bruger får noget data fra en private variable
"""