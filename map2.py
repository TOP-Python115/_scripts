from random import randrange as rr
from string import punctuation

def map(func, iterable):
    res = []
    for el in iterable:
        res += [func(el)]
    return res

def has_punct(word):
    for c in word:
        if c in punctuation:
            return False
    return True


l = input().split()
ml = map(has_punct, l)

print("words hasn't punctuation chars" 
            if all(ml) else 
      "words has punctuation chars")
