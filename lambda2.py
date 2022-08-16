from random import randint as ri
from pprint import pprint

l = [(ri(-10, 10), ri(0, 50)) for _ in range(20)]

l_sort0 = sorted(l)
l_sort1 = sorted(l, key=lambda l_element: l_element[1])

l_filt = list(filter(lambda l_element: True if l_element[0] >=0 else False, l))

l_map = list(map(lambda l_element: sum(l_element), l))
