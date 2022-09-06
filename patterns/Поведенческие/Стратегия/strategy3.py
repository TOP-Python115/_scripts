from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class Item(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LIZARD = 'lizard'
    SPOK = 'spok'

    @classmethod
    def rand(cls):
        return choice(list(cls))


class Tie(Exception):
    pass


class Strategy(ABC):
    item: Item

    # метод нарушает OCP
    @staticmethod
    @abstractmethod
    def check(other: Item) -> bool:
        pass


class Rock(Strategy):
    item = Item.ROCK

    # метод нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.SCISSORS:
            return True
        elif other is Item.PAPER:
            return False
        elif other is Item.ROCK:
            raise Tie


class Paper(Strategy):
    item = Item.PAPER

    # метод нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.ROCK:
            return True
        elif other is Item.SCISSORS:
            return False
        elif other is Item.PAPER:
            raise Tie


class Scissors(Strategy):
    item = Item.PAPER

    # метод нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER:
            return True
        elif other is Item.ROCK:
            return False
        elif other is Item.SCISSORS:
            raise Tie


# масштабирование
class Lizard(Strategy):
    item = Item.LIZARD

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER or other is Item.SPOK:
            return True
        elif other is Item.ROCK or other is Item.SCISSORS:
            return False
        elif other is Item.LIZARD:
            raise Tie


class Random(Strategy):
    item = Item.rand()

    # метод нарушает OCP
    @classmethod
    def check(cls, other: Item) -> bool:
        if cls.item is Item.ROCK:
            return Rock.check(other)
        elif cls.item is Item.PAPER:
            return Paper.check(other)
        elif cls.item is Item.SCISSORS:
            return Scissors.check(other)


class Player:
    def __init__(self, name: str, strategy: Strategy = None):
        self.name = name.upper()
        if strategy is None:
            self.strategy = Random()
        else:
            self.strategy = strategy

    def play(player1, player2: 'Player'):
        try:
            if player1.strategy.check(player2.strategy.item):
                return f'{player1.name} WINS'
            else:
                return f'{player2.name} WINS'
        except Tie:
            return 'TIE'



ivan = Player('ivan', Rock())
artem = Player('artem')

print(f'{ivan.name}: {ivan.strategy.item.name}')
print(f'{artem.name}: {artem.strategy.item.name}')

print(ivan.play(artem))
