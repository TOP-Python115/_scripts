class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(C):
    pass


def checkparents(obj):
    res = tuple()
    if obj.__bases__:
        res += checkparents(obj.__bases__[0])
    res += (obj,)
    return res

print(checkparents(D))
