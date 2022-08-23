
def mymap(func: "function", iter: tuple):
    """Грубое приближение встроенной функции map().

    Попытка воспроизвести работу встроенной функции map() без использования генераторов."""
    res = tuple()
    for el in iter:
        res += (func(el),)
    return res


def fx(x: float) -> float:
    """Полиномиальная функция с n = 2."""
    return x ** 2 - 4 * x + 3


def gxy(x: float, y: float = 0) -> float:
    """Полиномиальная функция двух переменных с n = m = 2."""
    return x ** 2 - y ** 2 + 5 * (y - x)


def hxy(*args):
    """Полиномиальная функция одной или двух переменных с n = m = 2."""
    x = args[0] if len(args) > 0 else 0
    y = args[1] if len(args) > 1 else 0
    return x ** 2 - y ** 2 + 5 * (y - x)


t = tuple(globals().values())
for obj in t:
    if callable(obj):
        print(obj.__name__)
        print(obj.__annotations__)
        print(obj.__doc__, end='\n\n')
