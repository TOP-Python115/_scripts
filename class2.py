class Rectangle:
    length = 0
    width = 0

r1 = Rectangle()
r1.length = 5
r1.width = 5

r2 = Rectangle()

# атрибут экземпляра
print(f'{r1.length = }')
# атрибут класса
print(f'{r2.length = }')
