from math import pi

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

r1 = Rectangle(10, 20)
print('до изменения r1.width', r1.__dict__)
r1.width = 20
print('после изменения r1.width', r1.__dict__, end='\n\n')
# площадь не изменилась, потому что данный атрибут рассчитывается один раз в конструкторе


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return round(pi*self.radius**2, 2)

c1 = Circle(5)
print('до изменения c1.width', f'{c1.area = }')
c1.radius = 7.5
print('после изменения c1.width', f'{c1.area = }', end='\n\n')
