from abc import ABC


class FruitVisitor:
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear
        }
        method = methods.get(fruit.__class__, self.draw_unknown)
        method()

    @staticmethod
    def draw_apple():
        print('яблоко')

    @staticmethod
    def draw_pear():
        print('груша')

    @staticmethod
    def draw_unknown():
        print('фрукт')


class Fruit(ABC):
    def draw(self, visitor: 'FruitVisitor'):
        visitor.draw(self)

class Apple(Fruit):
    pass

class Pear(Fruit):
    pass

class Banana(Fruit):
    pass



fv = FruitVisitor()

apple = Apple()
apple.draw(fv)

pear = Pear()
pear.draw(fv)

banana = Banana()
banana.draw(fv)

type(apple)
