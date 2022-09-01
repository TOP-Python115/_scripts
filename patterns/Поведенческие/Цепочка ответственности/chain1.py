from typing import Optional


class Creature:
    def __init__(self, name: str, default_attack: int, default_defense: int):
        self.name = name
        self.attack = default_attack
        self.defense = default_defense

    def __str__(self):
        return f'{self.name}: A={self.attack} / D={self.defense}'


class CreatureModifier:
    """Класс цепочки, запускает обработку данных."""
    def __init__(self, creature: Creature):
        self.creature = creature
        self.previous_modifier: Optional[CreatureModifier] = None
        self.next_modifier: Optional[CreatureModifier] = None

    def add_modifier(self, modifier: 'CreatureModifier'):
        if self.next_modifier is None:
            self.next_modifier = modifier
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(modifier)

    # def __del__(self):
    #     self.previous_modifier.next_modifier = self.next_modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    """Элемент цепочки, обрабатывает данные."""
    def handle(self):
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    """Элемент цепочки, обрабатывает данные."""
    def handle(self):
        if self.creature.attack <= 2:
            self.creature.defense += 1
        super().handle()

class StopModifier(CreatureModifier):
    def handle(self):
        print(f'No more bonuses for {self.creature.name}')


goblin = Creature('Goblin', 1, 1)
print(goblin)

root = CreatureModifier(goblin)

root.add_modifier(DoubleAttackModifier(goblin))
root.add_modifier(IncreaseDefenseModifier(goblin))
root.add_modifier(sm := StopModifier(goblin))
root.add_modifier(DoubleAttackModifier(goblin))
root.add_modifier(IncreaseDefenseModifier(goblin))
root.add_modifier(DoubleAttackModifier(goblin))
root.handle()
print(goblin)
