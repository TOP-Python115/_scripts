from operator import *
from functools import reduce
from random import randrange as rr, choice


l = [choice((rr(-3,0), rr(1, 4))) for _ in range(int(input()))]

agr_sum = reduce(add, l)
agr_prod = reduce(mul, l)

print(*l)
print(f'\n{agr_sum = }\n{agr_prod = }')
