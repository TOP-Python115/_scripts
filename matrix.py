from pprint import pprint

class Matrix:
    def __init__(self, n: int, m: int, fill: float = 0):
        self.rows = n
        self.cols = m
        self._straight = tuple((fill,)*m for _ in range(n))
        self._transposed = self._straight
        
    @property
    def straight(self):
        return self._straight
    
    @property
    def transposed(self):
        return self._transposed
    
    
    
    def __str__(self):
        mx = max([len(str(num)) for row in self._straight for num in row]) + 1
        return '\n'.join(''.join(f'{num:>{mx}}' for num in row) 
                         for row in self._straight)


m1 = Matrix(3, 3)
print(m1.rows)
print(m1.cols)
