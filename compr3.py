s = "0.98 1.12 0.56 0.57 0.91 1.5 0.62 0.74 1.3 1.04"

# slower
f = list(map(float, s.split()))
# faster
f = [float(n) for n in s.split()]

sn = sum(f)
res = [((n**2)/(sn**2))**0.5 for n in f]

print(*res)
