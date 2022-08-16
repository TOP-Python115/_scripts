class Triangle:
    a = -1
    b = -1
    c = -1
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return round((p*(p - self.a)*(p - self.b)*(p - self.c))**0.5, 1)


t1 = Triangle()
t1.a = 3
t1.b = 4
t1.c = 5
print(t1.perimeter())
print(t1.area())

t2 = Triangle()
print(t2.perimeter())
print(t2.area())
