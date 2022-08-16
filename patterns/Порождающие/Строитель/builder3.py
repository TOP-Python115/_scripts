"""Комбинированный строитель"""

class Person:
    def __init__(self):
        # адрес
        self.street = None
        self.city = None
        self.postcode = None
        # место работы
        self.company = None
        self.position = None
        self.income = None
    
    def __str__(self):
        return (f"Адрес: {self.street}, {self.city}, {self.postcode}\n"
                f"Место работы: {self.company}, {self.position}, {self.income}")


class PersonBuilder:
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person
    
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    
    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
        
    def at(self, company_name: str):
        self.person.company = company_name
        return self
    
    def as_a(self, position: str):
        self.person.position = position
        return self
    
    def earns(self, income: int):
        self.person.income = income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address: str):
        self.person.street = street_address
        return self
    
    def in_a(self, city: str):
        self.person.city = city
        return self
    
    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self


pers1 = PersonBuilder()\
    .works\
        .at('TOP')\
        .as_a('Teacher')\
        .earns(100)\
    .lives\
        .at('5 Bauman str')\
        .in_a('Ekaterinburg')\
        .with_postcode('620001')\
    .build()

pers2 = PersonBuilder()\
    .works\
        .at('ABC')\
        .as_a('Developer')\
        .earns(10000)\
    .lives\
        .at('23 Prospect')\
        .in_a('Fort Lauderdale')\
        .with_postcode('FL21')\
    .build()

print(pers1)
print(pers2)
