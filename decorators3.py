"""Декоратор для декоратора."""

from typing import Callable
from random import randrange as rr


def modifier(decorator: Callable):
    def _wrapper(*args, **kwargs):
        def __wrapper(func_to_decorate: Callable):
            print('\tаргументы для декоратора', *args)
            print('\tаргументы для декоратора', **kwargs)
            return decorator(func_to_decorate, *args, **kwargs)
        return __wrapper
    return _wrapper


# @modifier
def autocaller(func_obj: Callable, n: int):
    def wrapper(*args, **kwargs):
        res = []
        for _ in range(n):
            res += [func_obj(*args, **kwargs)]
        if sum(res) / len(res) == res[0]:
            return True
        else:
            return False
    return wrapper
autocaller = modifier(autocaller)


# @autocaller(3)
def test():
    return rr(1, 10)
test = autocaller(3)(test)
print(test())
