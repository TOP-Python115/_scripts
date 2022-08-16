
f = [i/100 for i in range(1, 100)]

res1 = [n for n in f if n > 0.75]

res2 = [n if 0.25 < n < 0.75 else 0 for n in f]


print(*res2, sep='\n')
