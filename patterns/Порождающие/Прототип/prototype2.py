from copy import copy, deepcopy


class Address:
    def __init__(self, city: str, street: str, suite: str):
        self.city = city
        self.street = street
        self.suite = suite

class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return (f'{self.name} lives on address: '
                f'{self.address.city}, {self.address.street}, {self.address.suite}')
    
    def clone(self):
        return deepcopy(self)


pers1 = Person('John', Address('Moscow', '5 Kutuzov Prospect', '15'))

pers2 = pers1.clone()
pers2.name = 'Maria'

pers3 = pers1.clone()
pers3.name = 'Oleg'
pers3.address.suite = '20'

print(f'{pers1 is pers2 = }')
print(pers1, pers2, pers3, sep='\n', end='\n\n')
