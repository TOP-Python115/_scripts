from random import randrange as rr
from time import perf_counter as pc, \
			   perf_counter_ns as npc

N = 5
l = [rr(0,10) for _ in range(10**N)]
t = tuple(rr(0,10) for _ in range(10**N))

start = pc()
for _ in range(10**N):
	a = l[::rr(1,10)]
end = pc()
print(f"Elapsed time for list: {end-start:.4f} s")

start = pc()
for _ in range(10**N):
	a = t[::rr(1,10)]
end = pc()
print(f"Elapsed time for tuple: {end-start:.4f} s")
