from math import pi

class Circle:
    def __init__(self, radius):
        # условно-приватное поле
        self._radius = radius
        # обращение к свойству (вызов геттера)
        # self.radius
        self._area = round(pi*radius**2, 2)
    
    # устновка свойства и геттер для свойства
    @property
    def area(self):
        return self._area
    
    # сеттер для соответствующего свойства
    @area.setter
    def area(self, area_val):
        self._area = area_val
        self._radius = round((area_val/pi)**0.5, 2)
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius_val):
        self._radius = radius_val
        self._area = round(pi*radius_val**2, 2)


c1 = Circle(5)
