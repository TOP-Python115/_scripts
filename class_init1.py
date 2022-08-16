class Triangle:
    name = 'triangle'
    
    def __init__(self, side1=1, side2=1, side3=1):
        self.a = side1
        self.b = side2
        self.c = side3
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return round((p*(p - self.a)*(p - self.b)*(p - self.c))**0.5, 1)


t1 = Triangle(3, 4, 5)
print(t1.perimeter())
print(t1.area())

t2 = Triangle()
# print(t2.perimeter())
# print(t2.area())
