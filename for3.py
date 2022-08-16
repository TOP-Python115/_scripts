sm = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 7 == 0:
        sm += i
    print(f'{i = }\t{sm = }')

print()

prod = 1
for i in range(1, 100):
    if i % 13 == 0:
        prod *= i
    print(f'{i = }\t{prod = }')
