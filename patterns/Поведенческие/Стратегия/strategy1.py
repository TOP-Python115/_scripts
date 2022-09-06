from typing import Callable
from operator import add, sub, mul


class Calculator:
    def __init__(self, number1: float, number2: float):
        self.number1 = number1
        self.number2 = number2

    def calculate(self, strategy: Callable) -> float:
        return strategy(self.number1, self.number2)


res = Calculator(2, 8).calculate(add)
print(f'{res = }')

res = Calculator(4, 5).calculate(sub)
print(f'{res = }')

res = Calculator(11, 5).calculate(mul)
print(f'{res = }')
