from random import randrange as rr

l1 = [rr(1, 10) for _ in range(int(input()))]
l2 = [rr(1, 10) for _ in range(int(input()))]
l3 = []


for i in range(len(l1)):
    if i < len(l2):
        if l1[i] > l2[i]:
            l3 += [l1[i]]
        else:
            l3 += [l2[i]]


for i in range(len(l1)):
    try:
        print(f'\nl1[{i}] = {l1[i]}')
        print(f'l2[{i}] = {l2[i]}')
        if l1[i] > l2[i]:
            l3 += [l1[i]]
        else:
            l3 += [l2[i]]
    except:
        break