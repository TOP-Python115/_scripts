from pprint import pprint

# передача аргумента по ссылке
def f1(numbers_list):
    res = numbers_list[:]
    i, v = map(int, input("f1(i, v): ").split())
    res[i] = v
    return res

def f2(numbers_list):
    res = numbers_list[:]
    i, v = map(int, input("f2(i, v): ").split())
    res[i] = v
    return res

def f3(numbers_list):
    res = numbers_list[:]
    i, v = map(int, input("f3(i, v): ").split())
    res[i] = v
    return res

def f4(numbers_list):
    res = numbers_list[:]
    i, v = map(int, input("f4(i, v): ").split())
    res[i] = v
    return res

def f5(numbers_list):
    res = numbers_list[:]
    i, v = map(int, input("f5(i, v): ").split())
    res[i] = v
    return res

# передача аргумента по значению
def f6(numbers_tuple):
    i, v = map(int, input("f5(i, v): ").split())
    q = list(numbers_tuple)
    q[i] = v
    return tuple(q)


n = [int(input(f"n[{i}]: ")) for i in range(5)]
print(n)
q = f5(f4(f3(f2(f1(n)))))

for i in range(1, 6):
    n = globals()[f"f{i}"]()
