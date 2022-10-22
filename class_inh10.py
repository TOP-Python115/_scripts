class NamedInt(int):
    __names = {0: 'zero',
               1: 'one',
               2: 'two',
               3: 'three',
               4: 'four',
               5: 'five',
               6: 'six',
               7: 'seven',
               8: 'eight',
               9: 'nine'}

    def __init__(self, value: int):
        self.name = self.__names[value]

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, int):
            new = super().__add__(other)
            if new < 10:
                return NamedInt(new)
            return new

    def __radd__(self, other):
        if isinstance(other, int):
            new = super().__add__(other)
            if new < 10:
                return NamedInt(new)
            return new


n1 = NamedInt(5)
n2 = NamedInt(3)
print(n1, type(n1), sep='\t')
print(n2, type(n2), sep='\t', end='\n')

n3 = n1 + n2
print(n3, type(n3), sep='\t')

n4 = n1 + n3
print(n4, type(n4), sep='\t')

n5 = n2 + 4
print(n5, type(n5), sep='\t')

n6 = 1 + n1
print(n6, type(n6), sep='\t')
