from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Wooden(Material):
    def __str__(self):
        return 'wooden'

class Cobblestone(Material):
    def __str__(self):
        return 'cobblestone'


class Building(ABC):
    @abstractmethod
    def print_name(self):
        pass

class Tower(Building):
    def __init__(self, name: str, material: Material):
        self.name = name
        self.material = material

    def print_name(self):
        print(str(self.material) + ' tower ' + self.name)

class Mill(Building):
    def __init__(self, name: str, mat1: Material, mat2: Material):
        self.name = name
        self.material1 = mat1
        self.material2 = mat2

    def print_name(self):
        print(' '.join((str(self.material1),
                        'and',
                        str(self.material2),
                        'mill',
                        self.name)))


borderland_tower = Tower('Eastland Tower', Cobblestone())
local_mill = Mill('Blue Creek Mill', Wooden(), Cobblestone())

borderland_tower.print_name()
local_mill.print_name()
