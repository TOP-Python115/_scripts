from random import randrange as rr
from string import ascii_lowercase as alc
from pprint import pprint

l = [list(alc[rr(0, 14):rr(13, 27)]) for _ in range(int(input()))]

nl = list(enumerate(l))
pprint(nl)
print()

d = dict(nl)
pprint(d)
print()

d = dict([(tuple(el[1]), el[0]) for el in nl])
pprint(d)
print()
