"""Наследуемый строитель"""

from datetime import date


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.birthdate = None

    def __str__(self):
        return (f"{self.name}: {self.position}, {self.birthdate}")


class PersonBuilder:
    def __init__(self):
        self.person = Person()
        
    def build(self):
        return self.person
    
class PersonNameBuilder(PersonBuilder):
    def called(self, name: str):
        self.person.name = name
        return self
        
class PersonJobBuilder(PersonNameBuilder):
    def works(self, position: str):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth: str):
        """date_of_birth: format YYYY-MM-DD"""
        self.person.birthdate = date.fromisoformat(date_of_birth)
        return self


pers1 = PersonBirthDateBuilder()\
        .works('STEP')\
        .born('1970-01-01')\
        .called('Adam')\
        .build()
print(pers1)
