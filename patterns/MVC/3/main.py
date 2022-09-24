from random import randrange as rr

MIN_ROW_COUNT = 5
MAX_ROW_COUNT = 30

MIN_COLUMN_COUNT = 5
MAX_COLUMN_COUNT = 30

MIN_MINES_COUNT = 1
MAX_MINES_COUNT = 800


class Cell:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.state = 'closed'
        self.mined = False
        self.counter = 0

    marks = ['closed', 'flagged', 'questioned']
    def next_mark(self):
        if self.state in self.marks:
            i = self.marks.index(self.state)
            self.state = self.marks[(i + 1) % len(self.marks)]

    def open(self):
        if self.state != 'flagged':
            self.state = 'opened'


# noinspection PyAttributeOutsideInit
class Model:
    def __init__(self):
        self.start()

    def start(self,
              row_count: int = 15,
              column_count: int = 15,
              mine_count: int = 15):
        if MIN_ROW_COUNT <= row_count <= MAX_ROW_COUNT:
            self.rows = row_count
        if MIN_COLUMN_COUNT <= column_count <= MAX_COLUMN_COUNT:
            self.columns = column_count
        if mine_count < self.rows * self.columns:
            if MIN_MINES_COUNT <= mine_count <= MAX_MINES_COUNT:
                self.mines = mine_count

        self.first_step = True
        self.game_over = False
        self.table = []
        for i in range(self.rows):
            self.table += [[]]
            for j in range(self.columns):
                self.table[i] += [Cell(i, j)]

    def generate_mines(self):
        for _ in range(self.mines):
            while True:
                cell = self.get_cell(rr(0, self.rows), rr(0, self.columns))
                if cell.state != 'opened' and not cell.mined:
                    cell.mined = True
                    break

    def get_cell(self, row_index: int, column_index: int):
        if not (0 <= row_index <= self.rows) or not (0 <= column_index <= self.columns):
            return None
        return self.table[row_index][column_index]

    def get_cells_neighbours(self, row_index: int, column_index: int):
        neighbours = []
        for i in range(row_index-1, row_index+2):
            neighbours += [self.get_cell(i, column_index-1)]
            if i != row_index:
                neighbours += [self.get_cell(i, column_index)]
            neighbours += [self.get_cell(i, column_index+1)]
        return filter(
            lambda cell: cell is not None,
            neighbours
        )

    def cell_next_mark(self, row_index: int, column_index: int):
        cell = self.get_cell(row_index, column_index)
        if cell:
            cell.next_mark()

    def is_win(self):
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.get_cell(i, j)
                if not cell.mined and cell.state != 'opened' and cell.state != 'flagged':
                    return False
        return True

    def is_game_over(self):
        return self.game_over

    def count_mines_around(self, row_index: int, column_index: int):
        neighbours = self.get_cells_neighbours(row_index, column_index)
        return sum(1 for cell in neighbours if cell.mined)

    def open_cell(self, row_index: int, column_index: int):
        cell = self.get_cell(row_index, column_index)
        if cell is None:
            return

        cell.open()

        if cell.mined:
            self.game_over = True
            return

        if self.first_step:
            self.first_step = False
            self.generate_mines()

        cell.counter = self.count_mines_around(row_index, column_index)

        if cell.counter == 0:
            for neighbor_cell in self.get_cells_neighbours(row_index, column_index):
                if neighbor_cell.state == 'closed':
                    self.open_cell(neighbor_cell.row, neighbor_cell.column)


m1 = Model()
