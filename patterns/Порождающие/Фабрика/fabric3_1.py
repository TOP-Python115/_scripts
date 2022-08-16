"""Фабрика"""

class Person:
    class PersonFactory:
        def __init__(self):
            self.id = 0
        
        def create_person(self, name):
            p = Person(self.id, name)
            self.id += 1
            return p

    factory = PersonFactory()
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"<Person {self.id}: {self.name}>"


pers1 = Person.factory.create_person('Alik')
pers2 = Person.factory.create_person('Jane')
pers3 = Person.factory.create_person('Goerge')
print(pers1, pers2, pers3, sep='\n')
