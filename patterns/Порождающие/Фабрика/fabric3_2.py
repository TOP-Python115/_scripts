"""Фабрика"""

class PersonFactory:
    __id = 0
    @classmethod
    def create_person(cls, name):
        p = Person(cls.__id, name)
        cls.__id += 1
        return p

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"<Person {self.id}: {self.name}>"


pers1 = PersonFactory.create_person('Alik')
pers2 = PersonFactory.create_person('Jane')
pers3 = PersonFactory.create_person('Goerge')
print(pers1, pers2, pers3, sep='\n')
