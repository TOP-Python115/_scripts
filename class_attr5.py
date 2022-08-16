class Person:
    def __init__(self, name, surname):
        self.name = name
        self._surname = surname
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str:
            self._name = value.title()
        else:
            raise TypeError('name should be str')



employee1 = Person('Anton', 'Ivanov')
