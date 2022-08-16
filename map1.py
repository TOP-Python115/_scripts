from random import randrange as rr

l = [rr(10, 100) for _ in range(int(input()))]

ml = list(map(lambda x: round((x**(2/3)-x)/(x-1), 2), l))

print(*l)
print(*ml)
