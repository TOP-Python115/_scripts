from random import randrange as rr
import sys

l1 = [rr(1, 10) for _ in range(int(input()))]
l2 = [rr(1, 10) for _ in range(int(input()))]
l3 = []

for i in range(len(l1)):
    try:
        print(f'\nl1[{i}] = {l1[i]}')
        print(f'l2[{i}] = {l2[i]}')
        if l1[i] > l2[i]:
            l3 += [l1[i]]
        else:
            l3 += [l2[i]]
    except Exception as E:
        print('except: Exception catched', E.args[0], sys.exc_info()[2])
        break
    else:
        print('else: all is fine')
    finally:
        print('finally: in all cases')
