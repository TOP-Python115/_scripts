"""Реализация шаблона Фасад для моделирования симуляции."""
from random import shuffle


class Hawk:
    def __init__(self):
        self.name = 'H'
        self.alive = True
        self.reproducing = False

    def __str__(self):
        return self.name

    @staticmethod
    def move() -> str:
        return 'attack'

    @staticmethod
    def reproduce() -> 'Hawk':
        return Hawk()


class Dove:
    def __init__(self):
        self.name = 'D'
        self.alive = True
        self.reproducing = False

    def __str__(self):
        return self.name

    @staticmethod
    def move() -> str:
        return 'defend'

    @staticmethod
    def reproduce() -> 'Dove':
        return Dove()


def iteration(species: list[Hawk | Dove]):
    half = len(species) // 2
    part1 = species[:half]
    part2 = species[half:]

    for a1, a2 in zip(part1, part2):
        move1, move2 = a1.move(), a2.move()

        if move1 == 'attack':
            if move2 == 'attack':
                a1.alive = False
                a2.alive = False
            elif move2 == 'defend':
                a2.alive = False
                a1.reproducing = True
        elif move1 == 'defend':
            if move2 == 'attack':
                a1.alive = False
                a2.reproducing = True
            elif move2 == 'defend':
                pass

    species = [a for a in part1 + part2 if a.alive]
    for animal in species:
        if animal.reproducing:
            species.append(animal.reproduce())

    return species


class Simulation:
    """Предоставляет дружественный интерфейс для проведения симуляций по объектной модели."""
    def __init__(self, hawk_number: int, dove_number: int):
        """Создаёт новую симуляцию.

        hawk_number: целое число ястребов в популяции;
        dove_number: целое число голубей в популяции."""
        self.population = []
        for _ in range(hawk_number):
            self.population += [Hawk()]
        for _ in range(dove_number):
            self.population += [Dove()]
        shuffle(self.population)

    def iterate(self) -> bool:
        """Выполняет один шаг симуляции. Возвращает True, если в популяции остались животные. Иначе — False."""
        self.population = iteration(self.population)
        shuffle(self.population)
        return bool(self.population)

    def show_animals(self) -> list:
        """Возвращает список животных в популяции."""
        return [str(a) for a in self.population]


s = Simulation(3, 15)
while s.iterate():
    print(s.show_animals())
