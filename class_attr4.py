class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, _):
        raise AttributeError('Change of name is denied')


employee1 = Person('Ivan', 'Ivanov')
