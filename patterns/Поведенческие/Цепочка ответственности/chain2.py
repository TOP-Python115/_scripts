# event broker
# command-query selector (cqs)
from abc import ABC, abstractmethod
from enum import Enum


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Query:
    def __init__(self,
                 creature_name: str,
                 what_to_query: WhatToQuery,
                 default_value: int):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self,
                      sender: 'Creature',
                      query: 'Query'):
        self.queries(sender, query)


class Creature:
    def __init__(self, game: Game, name: str, attack: int, defense: int):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name}: A={self.attack}/D={self.defense}"


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender: 'Creature', query: Query):
        pass


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: 'Creature', query: Query):
        if self.creature.name == sender.name:
            if query.what_to_query is WhatToQuery.ATTACK:
                query.value *= 2

class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: 'Creature', query: Query):
        if self.creature.name == sender.name:
            if query.what_to_query is WhatToQuery.DEFENSE:
                query.value += 1


new_game = Game()
goblin = Creature(new_game, 'Strong goblin', 2, 1)
print(goblin)

dam = DoubleAttackModifier(new_game, goblin)
print(goblin)
