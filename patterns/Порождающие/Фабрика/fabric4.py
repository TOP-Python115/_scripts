"""Фабрика"""

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def calculate_risk(self) -> int:
        pass

class Worker(Person):
    def __init__(self, name: str, age: int, hours: int):
        self.name = name
        self.age = age
        self.hours = hours
    
    def calculate_risk(self) -> int:
        return self.age * self.hours // 100

    def __str__(self):
        return f"{self.name.title()}: {self.hours} ч/неделю"

class Unemployed(Person):
    def __init__(self, name: str, age: int, able: bool):
        self.name = name
        self.age = age
        self.able = able
    
    def calculate_risk(self) -> int:
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self):
        if self.able:
            return f"{self.name.title()}: работоспособен"
        else:
            return f"{self.name.title()}: неработоспособен"


class PersonFactory:
    """Фабрика, которая получает указание на тип создаваемого объекта и запускает нужные механизмы сбора данных для каждого типа."""
    @staticmethod
    def create_person(person_type: str):
        person_type = person_type.lower()
        if person_type == 'worker':
            # в общем случае здесь находится механизм сбора данных
            name = 'Иван'
            age = 22
            hours = 30
            return Worker(name, age, hours)
        elif person_type == 'unemployed':
            # в общем случае здесь находится механизм сбора данных
            name = 'Екатерина'
            age = 30
            able = False
            return Unemployed(name, age, able)
        else:
            raise ValueError('person type is unknown')


pers1 = PersonFactory.create_person('worker')
pers2 = PersonFactory.create_person('unemployed')
print(pers1, pers2, sep='\n')
