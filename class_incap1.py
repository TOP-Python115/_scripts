class Test:
    def __init__(self, par1, par2):
        self.__a = par1
        self._b = par2

    def achange(self, val):
        self.__a = val
        
    def _sum(self):
        return sum(self.__container())
        
    def __container(self):
        return (self.__a, self._b)


t1 = Test(1, 2)
# приведёт к исключению
print(t1.__a)
t1.__a = 5
# допустимо
t1.achange(5)
# допустимо, но нежелательно
print(t1._b)
t1._b = 6
# допустимо
print(t1._sum())
# приведёт к исключению
print(t1.__container())
