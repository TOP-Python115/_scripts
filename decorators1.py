from math import prod
from time import perf_counter as pc

def withlen(func):
    def _wrapper(*args, **kwargs):
        return len(args), func(*args, **kwargs)
    return _wrapper

def timer(func):
    def _wrapper(*args, **kwargs):
        start = pc()
        _f = func(*args, **kwargs)
        stop = pc()
        print(f'Elapsed time for {func.__name__}: {stop-start:.4f} s\n')
        return _f
    return _wrapper

@timer
@withlen
def average(*args, mode='a'):
    if mode == 'a':
        return round(sum(args) / len(args), 2)
    elif mode == 'g':
        return round(prod(args)**(1/len(args)), 2)

@timer
def summ(*args):
    return sum(args)


a = average(*range(10**6))
g = average(*range(10**6), mode='g')
s = summ(*range(10**7))
