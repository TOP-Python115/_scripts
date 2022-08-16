from random import randrange as rr

class Warrior:
    health = 100
    
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name} attacks")
    
    def underattack(self):
        self.health = self.health - 20
        print(f"{self.name} is under attack: health = {self.health}")


duel = (Warrior('Ilya'), Warrior('Solovey'))

while all(w.health for w in duel):
    i = rr(2)
    duel[i].attack()
    duel[i-1].underattack()
    print()

