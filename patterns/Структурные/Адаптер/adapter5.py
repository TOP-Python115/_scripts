from collections.abc import Callable


class Dog:
    def __init__(self):
        self.name = 'Собака'

    def bark(self):
        return 'гав'

class Cat:
    def __init__(self):
        self.name = 'Кошка'

    def meow(self):
        return 'мяу'

class Human:
    def __init__(self):
        self.name = 'Человек'

    def speak(self):
        return 'привет'

class Car:
    def __init__(self):
        self.name = 'Машина'

    def make_noise(self, speed: int):
        return 'вр' + 'у'*(speed//20) + 'м'


class Adapter:
    def __init__(self, obj, **method: Callable):
        self.obj = obj
        self.__dict__.update(method)

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def original_dict(self):
        return self.obj.__dict__


creatures = [
    Adapter(dog := Dog(), make_noise=dog.bark),
    Adapter(cat := Cat(), make_noise=cat.meow),
    Adapter(man := Human(), make_noise=man.speak),
    Adapter(car := Car(), make_noise=lambda speed=60: car.make_noise(speed))
]
for cr in creatures:
    print(f"{cr.name} говорит {cr.make_noise()}")
print()

print(creatures[0].name)
print(creatures[1].__dict__)
print(creatures[2].original_dict())
print(creatures[3].make_noise(100))
