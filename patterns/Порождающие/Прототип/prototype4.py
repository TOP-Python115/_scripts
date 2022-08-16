from copy import deepcopy
from time import sleep, perf_counter as pc


class Address:
    def __init__(self, city: str, street: str, suite: str):
        self.city = city
        self.street = street
        self.suite = suite

class Employee:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address
        sleep(5)
    
    def __str__(self):
        return (f'{self.name} работает по адресу: '
                f'{self.address.city}, {self.address.street}, {self.address.suite}')
    
    @staticmethod
    def new_in_mainoffice(name: str, suite: str):
        return EmployeeFactory.new_mainoffice_empl(name, suite)
    
    @staticmethod
    def new_in_auxoffice(name: str, suite: str):
        return EmployeeFactory.new_auxoffice_empl(name, suite)


class EmployeeFactory:
    main_office_empl = Employee('', Address('Екатеринбург', 'пр. Космонавтов 28', ''))
    aux_office_empl = Employee('', Address('Севастополь', 'ул. Гоголя 16', ''))
    
    @staticmethod
    def __new_employee(proto: Employee, name: str, suite: str) -> Employee:
        new_empl = deepcopy(proto)
        new_empl.name = name
        new_empl.address.suite = suite
        return new_empl
    
    @classmethod
    def new_mainoffice_empl(cls, name: str, suite: str) -> Employee:
        return cls.__new_employee(cls.main_office_empl, name, suite)
    
    @classmethod
    def new_auxoffice_empl(cls, name: str, suite: str) -> Employee:
        return cls.__new_employee(cls.aux_office_empl, name, suite)

start = pc()
staff = [
    Employee.new_in_mainoffice('Андрей', '315'),
    EmployeeFactory.new_mainoffice_empl('Инна', '316'),
    Employee.new_in_auxoffice('Георгий', '122'),
    EmployeeFactory.new_auxoffice_empl('Вита', '122'),
    Employee.new_in_auxoffice('Никодим', '123')
]
stop = pc()
print(f'{stop - start:.3f} s')
print(*staff, sep='\n')
