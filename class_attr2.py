from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return round(pi*self.radius**2, 2)
    
    @area.setter
    def area(self, area_value):
        self.radius = round((area_value/pi)**0.5, 2)


c1 = Circle(5)
print('до изменения c1.width', f'{c1.area = }')
c1.radius = 7.5
print('после изменения c1.width', f'{c1.area = }', end='\n\n')

# c1.area = 100
