from random import randrange as rr
from string import punctuation

def filter(comparator, iterable):
    res = []
    for el in iterable:
        if comparator(el):
            res += [el]
    return res

def isverb(x):
    if x[-3:] == 'ing' and len(x) > 4:
        return True
    elif x[-2:] == 'ed' and len(x) > 3:
        return True
    else:
        return False

words = input().split()
words_long = filter(lambda x: len(x) > 2, words)
words_verbs = filter(isverb, words_long)

print(*words_long)
print(*words_verbs)
