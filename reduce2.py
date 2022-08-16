from operator import *
from functools import reduce
from random import randrange as rr, choice

def sum_of_prods(x, y):
    # print(f'{x = }\t{y = }')
    return (x[0]*y[0] + x[1]*y[1], 1)


n = int(input())
l = list(zip([rr(1, 5) for _ in range(n)], [rr(1, 5) for _ in range(n)]))

agr_sum_of_prods = reduce(sum_of_prods, l)[0]

print(*l)
print(f'\n{agr_sum_of_prods = }')
