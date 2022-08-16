class Table:
    def __init__(self, w, d, h):
        self.width = w
        self.depth = d
        self.height = h


class DeskTable(Table):
    def desk_area(self):
        return self.width * self.depth


class ComputerTable(DeskTable):
    def desk_area(self, monitor=0):
        return self.width * self.depth - monitor


ct1 = ComputerTable(90, 70, 85)
print(f'{ct1.desk_area() = }')
print(f'{ct1.desk_area(500) = }')
