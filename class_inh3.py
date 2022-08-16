class Table:
    def __init__(self, w=0, d=0, h=0):
        self.width = w
        self.depth = d
        self.height = h


class DeskTable(Table):
    def desk_area(self):
        return self.width * self.depth


class ComputerTable(DeskTable):
    def __init__(self, w=0, d=0, h=0, ks=0):
        super().__init__(w, d, h)
        self.keyboard_shelf = ks
    
    def check_keyboard_shelf(self, ks):
        self.keyboard_shelf = ks
    
    def desk_area(self, monitor=0):
        return self.width * self.depth - monitor


ct1 = ComputerTable(90, 70, 85, True)