from math import prod

def withlen(func):
    def _wrapper(*args, **kwargs):
        return len(args), func(*args, **kwargs)
    return _wrapper

@withlen
def average(*args, mode='a'):
    if mode == 'a':
        return round(sum(args) / len(args), 2)
    elif mode == 'g':
        return round(prod(args)**(1/len(args)), 2)


a = average(*range(10**6))
g = average(*range(10**6), mode='g')
