from random import randrange as rr

class Table:
    def __init__(self, columns):
        self.__columns = columns
        for i in range(1, columns+1):
            Table.__setattr__(self, f'_col{i}', [])

    def addvaltocol(self, column_index, value):
        Table.__setattr__(self, f'_col{column_index}', 
                          Table.__getattribute__(self, f'_col{column_index}') + [value])
    
    def __row(self, row_index):
        try:
            return tuple(Table.__getattribute__(self, f'_col{i}')[row_index] 
                         for i in range(1, self.__columns+1))
        except IndexError:
            return tuple()
    
    def __mincol(self):
        return min(len(Table.__getattribute__(self, f'_col{i}'))
                   for i in range(1, self.__columns+1))
   
    def tableaverage(self):
        filled_rows = self.__mincol()
        return round(sum(round(sum(self.__row(i)) / self.__columns, 3) 
                         for i in range(filled_rows)) / filled_rows, 3)


tb1 = Table(3)

# __setattr__
tb1._col1 = []
# __getattribute__
a = tb1._col1

for i in range(1, 4):
    tb1.addvaltocol(i, rr(10))

tb1.tableaverage()
