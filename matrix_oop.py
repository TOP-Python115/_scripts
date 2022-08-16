from functools import lru_cache
from random import randrange as rr


class MatrixError(Exception):
    pass

class IteratorNotMatrixError(MatrixError):
    def __init__(self):
        super().__init__("the argument should contain iterators of the same length")

class DimensionError(MatrixError):
    def __init__(self, 
                 message: str = '', 
                 dim1: tuple[int, int] = None, 
                 dim2: tuple[int, int] = None,
                 *args):
        if dim1 and dim2:
            message = f"can't use this operation for matrices of {dim1} dimension and {dim2} dimension"
            super().__init__(message, *args)
        else:
            super().__init__(message, *args)


class Matrix:
    def __init__(self, matrix):
        if self.__is_valid(matrix):
            self.n = len(matrix)
            self.m = len(matrix[0])
            self.origin = tuple(tuple(row) for row in matrix)
    
    @staticmethod
    def __is_valid(matrix):
        """..."""
        q = set(len(row) for row in matrix)
        if len(q) == 1 and 0 not in q:
            return True
        else:
            raise IteratorNotMatrixError
    
    @property
    @lru_cache(maxsize=1)
    def transposed(self):
        """..."""
        return tuple(tuple(self.origin[i][j] 
                           for i in range(self.n)) 
                     for j in range(self.m))
    
    @property
    @lru_cache(maxsize=1)
    def main_diag(self):
        """..."""
        return tuple(self.origin[i][i] 
                     for i in range(min(self.n, self.m)))
    
    @property
    @lru_cache(maxsize=1)
    def anti_diag(self):
        """..."""
        return tuple(self.origin[i][self.m-i-1] 
                     for i in range(min(self.n, self.m)))
    
    @property
    @lru_cache(maxsize=1)
    def __flat(self):
        """..."""
        return (num for row in self.origin for num in row)
    
    def __repr__(self):
        return f"Matrix {self.n}x{self.m}: ({self.origin[0]}, ...)"
    
    def __str__(self):
        max_width = max(len(str(num)) for num in self.__flat) + 1
        return '\n'.join(''.join(f'{num:>{max_width}}' for num in row) 
                         for row in self.origin)

    def __add__(self, value):
        if not isinstance(value, Matrix):
            raise TypeError(f"can't add objects of types '{self.__class__.__name__}' and '{value.__class__.__name__}'")
        if not self.n == value.n or not self.m == value.m:
            # raise DimensionError("can't add matrices of different dimensions")
            raise DimensionError('',
                                 (self.n, self.m),
                                 (value.n, value.m),
                                 1, 2)
        return self.__add(value)
    
    def __sub__(self, value):
        if not isinstance(value, Matrix):
            raise TypeError(f"can't substract '{self.__class__.__name__}' and '{value.__class__.__name__}'")
        if not self.n == value.n or not self.m == value.m:
            raise DimensionError("can't substract matrices of different dimensions")
        return self.__add(value, '-')
        
    def __add(matr1, value, operation='+'):
        """..."""
        res = []
        for i in range(matr1.n):
            res += [[]]
            for j in range(matr1.m):
                if operation == '+':
                    res[i] += [ matr1.origin[i][j] + value.origin[i][j] ]
                elif operation == '-':
                    res[i] += [ matr1.origin[i][j] - value.origin[i][j] ]
                elif operation == '*':
                    res[i] += [ matr1.origin[i][j] * value ]
        return Matrix(res)

    def __mul__(self, value):
        if not isinstance(value, Matrix):
            if isinstance(value, (int, float)):
                return self.__add(value, '*')
            else:
                raise TypeError(f"can't multiply '{self.__class__.__name__}' and '{value.__class__.__name__}'")
        # TODO: умножение матриц
    
    def __radd__(self, value):
        if not isinstance(value, Matrix):
            raise TypeError(f"can't add objects of types '{self.__class__.__name__}' and '{value.__class__.__name__}'")

    def __rsub__(self, value):
        if not isinstance(value, Matrix):
            raise TypeError(f"can't substract '{self.__class__.__name__}' and '{value.__class__.__name__}'")

    def __rmul__(self, value):
        if not isinstance(value, Matrix):
            if isinstance(value, (int, float)):
                return self.__add(value, '*')
            else:
                raise TypeError(f"can't multiply '{self.__class__.__name__}' and '{value.__class__.__name__}'")
        # TODO: умножение матриц

    def __contains__(self, value):
        if isinstance(value, (int, float)):
            return value in self.__flat


m1 = Matrix([[rr(0, 10) for _ in range(4)] for _ in range(3)])
m2 = Matrix([[rr(0, 10) for _ in range(3)] for _ in range(4)])
print(m1, m2, sep='\n\n', end='\n\n\n')

# m3 = m1 * 3
# m4 = 2 * m2
# print(m3, m4, sep='\n\n', end='\n\n')

# print(1 in m1)
