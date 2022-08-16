from random import randrange as rr

l = [rr(0, 2) for _ in range(int(input('list len: ')))]
print(l)
print(f'{all(l) = }')
print(f'{any(l) = }')
