def printed(func):
    def _wrapper():
        print(f'до вызова функции {func.__name__}')
        func()
        print(f'после вызова функции {func.__name__}')
    return _wrapper


def testfunc():
    print(f'выполнение функции {testfunc}')

testfunc = printed(testfunc)
print(type(testfunc), testfunc.__name__)
testfunc()


@printed
def testfunc2():
    print(f'выполнение функции {testfunc}')

testfunc2()
