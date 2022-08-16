l = [1, 2, 3, 4, 1, 6, 8, 2, 1, 5, 6]
s = set()

for e in l:
    if e not in s:
        print(f"{e} NO")
        s.add(e)
    else:
        print(f"{e} YES")
