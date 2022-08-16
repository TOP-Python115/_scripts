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


pers1 = Person('John', Address('Moscow', '5 Kutuzov Prospect', '15'))
print(pers1, end='\n\n')

pers2 = pers1
pers2.name = 'Ivan'
print(f'{pers1 is pers2 = }')
print(pers1, pers2, sep='\n', end='\n\n')

pers3 = copy(pers1)
pers3.name = 'Maria'
pers3.address.suite = '16'
print(f'{pers1 is pers3 = }')
print(pers1, pers3, sep='\n', end='\n\n')

pers4 = deepcopy(pers1)
pers4.name = 'Elena'
pers4.address.suite = '17'
print(f'{pers1 is pers4 = }')
print(pers1, pers4, sep='\n', end='\n\n')
