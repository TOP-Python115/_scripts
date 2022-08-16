class Character:
    def __init__(self, health, armor, attack):
        self.health = health
        self.armor = armor
        self.attack = attack
    
    def move(self, value):
        print(f'двигается на {value} клеток')


class Hero(Character):
    def __init__(self, health, armor, attack, name, class_):
        super().__init__(health, armor, attack)
        self.name = name
        self.class_ = class_
        self.army = []
    
    def move(self, value):
        super().move(value)
        for soldier in self.army:
            soldier.move(value)


class Soldier(Character):
    def __init__(self, health, armor, attack, id):
        super().__init__(health, armor, attack)
        self.id = id
    
    def __repr__(self):
        return f"soldier {self.id}"


from random import randrange as rr


z = Hero(100, 50, 60, 'Zygfrid', 'Warrior')
m = Hero(80, 30, 50, 'Merlin', 'Wizard')

z.army += [Soldier(rr(90, 111, 10),
                   rr(40, 51, 10),
                   rr(40, 61, 10),
                   f'{i+1:>{0}3}') 
           for i in range(rr(4, 7))]

m.army += [Soldier(rr(90, 111, 10),
                   rr(40, 51, 10),
                   rr(40, 61, 10),
                   f'{i+1:>{0}3}') 
           for i in range(rr(4, 7))]

z_th = z.health + sum([s.health for s in z.army])
m_th = m.health + sum([s.health for s in m.army])

print(z.name, z.army, f'Total health: {z_th}', sep='\n', end='\n\n')
print(m.name, m.army, f'Total health: {m_th}', sep='\n', end='\n\n')

if z_th > m_th:
    print(z.name, 'победил!')
elif z_th < m_th:
    print(m.name, 'победил!')
else:
    print('силы равны')
