class Room:
    def __init__(self, w, d, h):
        self.walls = Walls(w, d, h)
        self.windoors = []
    
    def add_windoor(self, w, h):
        self.windoors += [WinDoor(w, h)]
    
    @property
    def area(self):
        return self.walls.area - sum(wd.area for wd in self.windoors)


class Walls:
    def __init__(self, w, d, h):
        self.width = w
        self.depth = d
        self.height = h
    
    @property
    def area(self):
        return 2*self.height*(self.width + self.depth)


class WinDoor:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    @property
    def area(self):
        return self.width*self.height


kitchen = Room(4, 6, 3)
kitchen.add_windoor(1.2, 2.2)
kitchen.add_windoor(1.8, 2)
print(kitchen.area)
