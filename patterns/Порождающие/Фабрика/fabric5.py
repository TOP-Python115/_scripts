"""Абстрактная фабрика"""

from abc import ABC, abstractmethod
from enum import Enum
from inspect import getmembers, isclass, isabstract
from sys import modules


class HotDrink(ABC):
    """Напитки, которые можно употребить."""
    DRINK = True
    @abstractmethod
    def consume(self):
        pass

class Tea(HotDrink):
    """Реализация чая."""
    def consume(self):
        print('Чай вкусный.')

class Coffee(HotDrink):
    """Реализация кофе."""
    def consume(self):
        print('Кофе вкусный.')

class Grog(HotDrink):
    """Реализация грога."""
    def consume(self):
        print('Грог вкусный.')


class HotDrinkFactory(ABC):
    """Абстрактный базовый класс, который в текущих обстоятельствах нужен только для указания необходимости реализации метода prepare()."""
    @abstractmethod
    def prepare(self, amount: int):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        # имитация сложного процесса
        print('Вскипятить воду.')
        print('Положить чайный пакетик в чашку.')
        print(f'Добавить {amount} мл кипятка.')
        print('Чай готов.')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        # имитация сложного процесса
        print('Смолоть несколько зерён кофе.')
        print('Вскипятить воду.')
        print(f'Добавить {amount} мл кипятка.')
        print('Кофе готов.')
        return Coffee()

class GrogFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        # имитация сложного процесса
        print('Заварить чифир.')
        print(f'Смешать {amount//2} мл чифира и {amount//2} мл рома.')
        print('Грог готов.')
        return Grog()


class HotDrinkMachine:
    """Модель автомата по приготовлению напитков. 
    
    Осуществляет сбор данных для последующего создания объекта."""
    # нарушение OCP
    # class AvailableDrinks(Enum):
        # Tea = 1
        # Coffee = 2
    # динамически формируемое перечисление напитков с номерами
    # существующие напитки берёт из соответствующих классов
    AvailableDrinks = \
        Enum('AvailableDrinks', 
             [pair[0] 
              for pair in getmembers(modules[__name__], 
                                     lambda obj: isclass(obj)
                                                 and getattr(obj, 'DRINK', False)
                                                 and not isabstract(obj))])
    # for elem in AvailableDrinks:
        # print(f"{elem.name} = {elem.value}")
    # словарь хранит экземпляры фабрик по ключам из перечисления AvailableDrinks
    factories = {}
    __initialized = False
    
    def __init__(self):
        if not self.__class__.__initialized:
            self.__class__.__initialized = True
            for drink in self.AvailableDrinks:
                self.__class__.factories[drink] = eval(f"{drink.name}Factory")()
    
    def show_drinks(self) -> None:
        """Показать все доступные напитки."""
        print('Напитки:')
        for drink in self.AvailableDrinks:
            print(f'\t{drink.value}. {drink.name}')
    
    def choose_type(self) -> int:
        """Запрос пользователю: вид напитка."""
        lf = len(self.AvailableDrinks)
        return int(input(f'Выберите напиток (1-{lf}): '))
    
    def choose_amount(self) -> int:
        """Запрос пользователю: объём напитка."""
        return int(input('Укажите количество напитка (мл): '))
    
    def make_drink(self) -> HotDrink:
        """Собирает все данные и вызывает метод для генерации объекта напитка от нужного экземпляра фабрики."""
        self.show_drinks()
        id = self.choose_type()
        amount = self.choose_amount()
        return self.factories[self.AvailableDrinks(id)].prepare(amount)


hdm = HotDrinkMachine()
hdm.make_drink().consume()
