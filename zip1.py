from random import randrange as rr
from string import ascii_lowercase as alc, ascii_uppercase as auc
from pprint import pprint

z = zip(alc, auc, range(0, 5))

print(*z)
