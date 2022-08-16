from random import randrange as rr, choice
from string import ascii_lowercase as alc

l = [(lambda c: c in alc)(i) for i in "asdef"]

print(l)

print(f'{all(l) = }')
print(f'{any(l) = }')
