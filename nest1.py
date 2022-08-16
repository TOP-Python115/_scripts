t = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12))

for row in t:
    for el in row:
        print(str(el).rjust(3), end='')
    print()
