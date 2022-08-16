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


class Duel:
    def __init__(self, w1_name, w2_name):
        self.opponents = (Warrior(w1_name), Warrior(w2_name))
    
    def start(self):
        while all(w.health for w in self.opponents):
            i = rr(2)
            self.opponents[i].attack()
            self.opponents[i-1].underattack()
            print()


d1 = Duel('Rodger', 'William')
d1.start()

d2 = Duel('Ilya Muromec', 'Solovey-Razboynik')
d2.start()
