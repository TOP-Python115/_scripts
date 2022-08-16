def func1():
    res = func2()
    return res

def func2():
    res = func3()
    return res

def func3():
    res = func4()
    return res

def func4():
    res = func5()
    return res

def func5():
    return 10

print(func1())
