# a**n = a * a**(n-1)
# a**(n-1) = a * a**(n-2)
# ...
# a**n = a * a * a * 1

# def power(base: int, exp):
#     """Рекурсивная функция возведения в степень.
#
#     Рекурсия — это круто! Но медленно..."""
#     if exp == 1:
#         return base
#     else:
#         return base * power(base, exp-1)
#
# print(power(int(input('base: ')), int(input('exp: '))))
#
#
# # a % d == 0
# # b % d == 0
#
# def gcd(a, b):
#     """Рекурсивная функция нахождения наибольшего общего делителя (НОД)"""
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
# print(gcd(int(input('a: ')), int(input('b: '))))


def recur_func(x: int) -> int:
    print(f"вызов recur_func c аргументом {x}")
    if x > 0:
        res = recur_func(x - 1)
        print(f"возврат {res}")
        return res
    else:
        print(f"первый возврат {x}")


print(recur_func(int(input('глубина рекурсии: '))))

