class People:
    def __init__(self, *people: Person):
        self.people = list(people)
    
    def add(self, person: Union[Person, Staff]):
        self.people.append(person)
    __add__ = add

    def __iter__(self):
        for i in self.people:
            yield [i.name, i.age]

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Staff(Person):
    def __init__(self, name:str, age:int, staff_id:int):
        super().__init__(name, age)
        self.staff_id = staff_id
