class A:
    all_objs = []
    
    def __init__(self):
        self.__class__.all_objs += [self]

class B(A):
    pass

class C(A):
    pass


bs = [B() for _ in range(3)]
cs = [C() for _ in range(2)]

