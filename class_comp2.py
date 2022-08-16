class Shape:
    all_shapes = tuple()
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__.all_shapes += (self, )


sh1 = Shape(0, 0)
sh2 = Shape(1, 2)

print(Shape.all_shapes)
print((sh1, sh2))
print(f'\n{(Shape.all_shapes == (sh1, sh2)) = }')
