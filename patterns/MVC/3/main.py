from random import randrange as rr
from tkinter import Tk, Frame, Button, StringVar, Spinbox, Label
from tkinter.constants import BOTTOM, X, RIGHT, TOP, LEFT, SUNKEN
from tkinter.messagebox import showinfo

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
        if not (0 <= row_index < self.rows) or not (0 <= column_index < self.columns):
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


# noinspection PyAttributeOutsideInit
class View(Frame):
    def __init__(self,
                 model: Model,
                 controller: 'Controller',
                 parent: Tk = None):
        Frame.__init__(self, parent)
        self.model = model
        self.controller = controller
        self.controller.set_view(self)
        self.create_board()

        ctrl_panel = Frame(self)
        ctrl_panel.pack(side=BOTTOM, fill=X)

        Button(
            ctrl_panel,
            text='Новая игра',
            command=self.controller.start_new_game
        ).pack(side=RIGHT)

        self.mine_count = StringVar(ctrl_panel)
        self.mine_count.set(str(self.model.mines))

        Spinbox(
            ctrl_panel,
            from_=MIN_MINES_COUNT,
            to=MAX_MINES_COUNT,
            textvariable=self.mine_count,
            width=5
        ).pack(side=RIGHT)

        Label(
            ctrl_panel,
            text=' Количество мин: '
        ).pack(side=RIGHT)

        self.row_count = StringVar(ctrl_panel)
        self.row_count.set(str(self.model.rows))

        Spinbox(
            ctrl_panel,
            from_=MIN_ROW_COUNT,
            to=MAX_ROW_COUNT,
            textvariable=self.row_count
        ).pack(side=RIGHT)

        Label(
            ctrl_panel,
            text=' x '
        ).pack(side=RIGHT)

        self.column_count = StringVar(ctrl_panel)
        self.column_count.set(str(self.model.columns))

        Spinbox(
            ctrl_panel,
            from_=MIN_COLUMN_COUNT,
            to=MAX_COLUMN_COUNT,
            textvariable=self.column_count
        ).pack(side=RIGHT)

        Label(
            ctrl_panel,
            text='Размер поля: '
        ).pack(side=RIGHT)

    def create_board(self):
        try:
            self.board.pack_forget()
            self.board.destroy()
            self.row_count.set(str(self.model.rows))
            self.column_count.set(str(self.model.columns))
            self.mine_count.set(str(self.model.mines))
        except AttributeError:
            pass

        self.board = Frame(self)
        self.board.pack()
        self.buttons_table = []
        for i in range(self.model.rows):
            line = Frame(self.board)
            line.pack(side=TOP)
            buttons_row = []
            for j in range(self.model.columns):
                btn = Button(
                    line,
                    width=2,
                    height=1,
                    command=lambda r=i, c=j: self.controller.on_left_click(r, c),
                    padx=0,
                    pady=0
                )
                btn.pack(side=LEFT)
                btn.bind(
                    '<Button-3>',
                    lambda e, r=i, c=j: self.controller.on_right_click(r, c)
                )
                buttons_row += [btn]
            self.buttons_table += [buttons_row]

    def sync_with_model(self):
        for i in range(self.model.rows):
            for j in range(self.model.columns):
                cell = self.model.get_cell(i, j)
                if cell:
                    btn = self.buttons_table[i][j]

                    if self.model.is_game_over() and cell.mined:
                        btn.config(bg='black', text='')

                    if cell.state == 'closed':
                        btn.config(text='')
                    elif cell.state == 'flagged':
                        btn.config(text='P')
                    elif cell.state == 'questioned':
                        btn.config(text='?')
                    elif cell.state == 'opened':
                        btn.config(relief=SUNKEN, text='')
                        if cell.counter > 0:
                            btn.config(text=cell.counter)
                        elif cell.mined:
                            btn.config(bg='red')

    def get_game_settings(self):
        return self.row_count.get(), self.column_count.get(), self.mine_count.get()

    def block_cell(self, row: int, column: int, block: bool = True):
        btn = self.buttons_table[row][column]
        if not btn:
            return

        if block:
            btn.bind('<Button-1>', 'break')
        else:
            btn.unbind('<Button-1>')

    @staticmethod
    def show_win_message():
        showinfo('Поздравляем!', 'Вы победили!')

    @staticmethod
    def show_game_over_message():
        showinfo('Игра окончена!', 'Вы проиграли!')


# noinspection PyAttributeOutsideInit
class Controller:
    def __init__(self, model: Model):
        self.model = model

    def set_view(self, view: View):
        self.view = view

    def start_new_game(self):
        settings = self.view.get_game_settings()
        try:
            self.model.start(*map(int, settings))
        except ValueError:
            self.model.start(self.model.rows, self.model.columns, self.model.mines)
        self.view.create_board()

    def on_left_click(self, row: int, column: int):
        self.model.open_cell(row, column)
        self.view.sync_with_model()
        if self.model.is_win():
            self.view.show_win_message()
            self.start_new_game()
        elif self.model.is_game_over():
            self.view.show_game_over_message()
            self.start_new_game()

    def on_right_click(self, row: int, column: int):
        self.model.cell_next_mark(row, column)
        self.view.block_cell(
            row, column,
            self.model.get_cell(row, column).state == 'flagged'
        )
        self.view.sync_with_model()


m1 = Model()
c1 = Controller(m1)
v1 = View(m1, c1)
v1.pack()
v1.mainloop()
