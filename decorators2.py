from typing import Callable


def decorator_generator(arg1, arg2):
    print('это генератор декораторов')
    print('он принял аргументы:', arg1, arg2)

    def decorator(func_obj: Callable):
        print('\tэто декоратор')
        print('\tон видит аргументы, переданные в генератор:', arg1, arg2)

        def wrapper(*args, **kwargs):
            print('\t\tэто обёртка декорируемой функции')
            print('\t\tона также видит аргументы, переданные в генератор:', arg1, arg2)
            res = func_obj(*args, **kwargs)
            print(f'\t\tэто возвращаемое значение декорируемой функции: {res}')
            return res

        return wrapper

    return decorator



def test():
    print('\t\t\tэто декорируемая функция')
    print('\t\t\tона видит только аргументы, переданные непосредственно ей')


# print()
# generated_decorator = decorator_generator(10, 20)
# print(f'{generated_decorator = }\n{type(generated_decorator) = }')
#
# print()
# decorated_test = generated_decorator(test)
# print(f'{decorated_test = }\n{type(decorated_test) = }')
#
# print()
# decorated_test()

test = decorator_generator(100, 200)(test)
test()
print('\n')


@decorator_generator('аргумент1', 'аргумент2')
def test2():
    print('\t\t\tэто вторая декорируемая функция')

