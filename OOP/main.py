# Klasser, nedarvning, properties, constructor, override
from classes import *

people = People(Person("Jørgen", 41), Person("Lene", 28))

def TestWorkingClasses():
    person = Person("Bo", 51)

    people.add(person)

    person2 = Person("Mogens", 81)

    people + person2

    PrintPeople()

def TestAbstractClass():
    abstractPerson = AbstractPerson()

    print(abstractPerson.return_self())

def TestExceptionHandling():
    while True:
        try:
            people + eval(input("Make me a class: "))
            break
        except Exception:
            print("Not valid person")

def PrintPeople():
    for person in people:
        print(person)