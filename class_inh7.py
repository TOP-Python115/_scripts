from pprint import pprint

class A1:
    def __init__(self):
        print(f'A1 constructor')

class C1:
    def __init__(self):
        print(f'C1 constructor')

class E1:
    def __init__(self):
        print(f'E1 constructor')

class B2(A1):
    pass
    # def __init__(self):
        # super().__init__()
        # print(f'B2 constructor')

class D2(C1):
    def __init__(self):
        super().__init__()
        print(f'D2 constructor')

class F2(C1, E1):
    def __init__(self):
        super().__init__()
        print(f'F2 constructor')

class G3(B2, D2):
    def __init__(self):
        super().__init__()
        print(f'G3 constructor')

class H3(B2, F2):
    def __init__(self):
        super().__init__()
        print(f'H3 constructor')
    
class I4(G3, H3):
    pass

class J4(H3, G3):
    pass


# print('\nF2 mro')
# pprint(F2.mro())

# print('\nG3 mro')
# pprint(G3.mro())

# print('\nH3 mro')
# pprint(H3.mro())

print('\nI4 mro')
pprint(I4.mro())

print()
i4 = I4()

print('\nJ4 mro')
pprint(J4.mro())

print()
j4 = J4()


