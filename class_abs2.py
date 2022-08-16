from abc import ABC, abstractmethod

# класс данных
class Goods:
    def __init__(self, name: str, 
                       color: str, 
                       size: str):
        self.name = name
        self.color = color.upper()
        self.size = size.upper()

# плохая реализация:
#  - требует изменения класса
#  - взрывной рост сложности расширения
class GoodsFilter:
    def __init__(self, goods):
        self.goods = goods
    
    def filter_by_color(self, color):
        for g in self.goods:
            if g.color == color.upper():
                yield g
    
    def filter_by_size(self, size):
        for g in self.goods:
            if g.size == size.upper():
                yield g
    
    def filter_by_color_and_size(self, color, size):
        for g in self.goods:
            if g.color == color.upper() and g.size == size.upper():
                yield g

# 2 criteria — 3 combines 
# (s, c): s c sc 

# 3 criteria — 7 combines
# (s, c, w): s c w sc sw cw scw

# 4 criteria — 15 combines
# (s, c, w, b): s c w b sc sw sb cw cb wb scw scb swb cwb scwb

# абстрактные базовые классы
class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass

class Filter(ABC):
    @abstractmethod
    def filter(self):
        pass

# классы расширения
class ColorSpec(Specification):
    def __init__(self, color):
        self.color = color.upper()
    
    def is_satisfied(self, item):
        return self.color == item.color

class SizeSpec(Specification):
    def __init__(self, size):
        self.size = size.upper()
    
    def is_satisfied(self, item):
        return self.size == item.size

class AndSpec(Specification):
    def __init__(self, *specs):
        self.specs = specs
    
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.specs
        ))

# класс реализация логики фильтрации
class BetterFilter(Filter):
    def __init__(self, goods):
        self.goods = goods
    
    def filter(self, specification):
        for g in self.goods:
            if specification.is_satisfied(g):
                yield g


products = (
    Goods('Apple', 'Green', 'small'),
    Goods('Tree', 'Green', 'Large'),
    Goods('House', 'Blue', 'Large')
)

gf = GoodsFilter(products)

print('\nGreen goods:')
for g in gf.filter_by_color('green'):
    print(f' - {g.name} is green')

print('\nLarge goods:')
for g in gf.filter_by_size('large'):
    print(f' - {g.name} is large')

print('\nLarge and green goods:')
for g in gf.filter_by_color_and_size('green', 'large'):
    print(f' - {g.name} is large and green')

bf = BetterFilter(products)

green = ColorSpec('green')
print('\nGreen goods:')
for g in bf.filter(green):
    print(f' - {g.name} is green')

large = SizeSpec('large')
print('\nLarge goods:')
for g in bf.filter(large):
    print(f' - {g.name} is large')

blue = ColorSpec('blue')
large_and_blue = AndSpec(large, blue)
print('\nLarge and blue goods:')
for g in bf.filter(large_and_blue):
    print(f' - {g.name} is large and blue')
