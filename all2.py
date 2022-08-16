from random import randrange as rr, choice
from string import ascii_lowercase as alc

l = [(lambda: choice((-1, 1)) > 0)() for _ in range(int(input('list len: ')))]

print(l)

print(f'{all(l) = }')
print(f'{any(l) = }')
