from time import perf_counter as pc
from math import prod

def timer(func):
    def _wrapper(*args, **kwargs):
        start = pc()
        _f = func(*args, **kwargs)
        stop = pc()
        print(f'Elapsed time for {func.__name__}: {stop-start:.4f} s\n')
        return _f
    return _wrapper

@timer
def average(*args, mode='a'):
    if mode == 'a':
        return round(sum(args) / len(args), 2)
    elif mode == 'g':
        return round(prod(args)**(1/len(args)), 2)


a = average(*range(5*10**6))
g = average(*range(5*10**6), mode='g')
