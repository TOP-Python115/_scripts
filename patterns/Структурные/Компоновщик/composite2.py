"""Рекурсивный компоновщик"""

from abc import ABC, abstractmethod
from typing import Iterable


class Item(ABC):
    @abstractmethod
    def return_price(self) -> int:
        pass


class Box(Item):
    def __init__(self, contents: Iterable):
        self.contents = contents

    def return_price(self) -> int:
        price = 0
        for item in self.contents:
            price += item.return_price()
        return price


class Phone(Item):
    def __init__(self, price: int):
        self.price = price

    def return_price(self) -> int:
        return self.price


class Charger(Item):
    def __init__(self, price: int):
        self.price = price

    def return_price(self) -> int:
        return self.price


class Earphones(Item):
    def __init__(self, price: int):
        self.price = price

    def return_price(self) -> int:
        return self.price


phone = Phone(52450)
package = Box([
    phone,
    Charger(2750),
    Earphones(5499)
])

print(f'Стоимость смартфона без аксессуаров: {phone.return_price()} ₽')
print(f'Стоимость смартфона с аксессуарами: {package.return_price()} ₽')
