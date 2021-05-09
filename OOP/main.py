#import classes
import classes

people = People(Person("Jørgen", 41), Person("Lene", 28))



person = Person("Bo", 51)

person.name, person.age

people.add(person)

person2 = Person("Mogens", 81)

people + person2

for person in people:
    print(person)