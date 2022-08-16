from copy import deepcopy
from time import sleep, perf_counter as pc

class Character:
    """Base class for game characters."""
    def __init__(self, 
                 name: str = None, 
                 age: int = None, 
                 attack: int = None, 
                 defense: int = None):
        # base character's attributes
        self.name = name
        self.age = age
        self.attack = attack
        self.defense = defense
        # imitation of long and complex instantiation
        sleep(2)
        
    def __repr__(self):
        return (f'<{self.name}: '
                f'age={self.age}, '
                f'attack={self.attack}, '
                f'defense={self.defense}>')
    
    def clone(self):
        return deepcopy(self)


class Warrior(Character):
    def __init__(self,
                 name: str = '',
                 age: int = 0,
                 attack: int = 0,
                 defense: int = 0,
                 stamina: int = 0):
        super().__init__(name, age, attack, defense)
        # subclass attribute
        self.stamina = stamina
    
    def __repr__(self):
        return super().__repr__()[:-1] + f', stamina={self.stamina}>'

class Mage(Character):
    def __init__(self,
                 name: str = '', 
                 age: int = 0, 
                 attack: int = 0, 
                 defense: int = 0,
                 mana: int = 0):        
        super().__init__(name, age, attack, defense)
        # subclass attribute
        self.mana = mana
    
    def __repr__(self):
        return super().__repr__()[:-1] + f', mana={self.mana}>'

class Trader(Character):
    def __init__(self,
                 name: str = '', 
                 age: int = 0, 
                 attack: int = 0, 
                 defense: int = 0,
                 harisma: int = 0):        
        super().__init__(name, age, attack, defense)
        # subclass attribute
        self.harisma = harisma
    
    def __repr__(self):
        return super().__repr__()[:-1] + f', harisma={self.harisma}>'


start = pc()
army = [Warrior() for _ in range(5)] + [Mage() for _ in range(2)] + [Trader()]
stop = pc()
print(f'Elapsed time for creating army: {stop-start:.3f} s')

start = pc()
w = Warrior('Soldier', 30, 50, 30)
m = Mage('Wizard', 50, 60, 10)
t = Trader('Supporter', 40, 10, 25)
army = [w.clone() for _ in range(5)] + [m.clone() for _ in range(2)] + [t.clone()]
stop = pc()
print(f'Elapsed time for cloning army: {stop-start:.3f} s\n')

print(*army, sep='\n')
