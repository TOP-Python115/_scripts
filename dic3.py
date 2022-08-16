# # пример ввода:
    # # Ирина Сапожникова 25 160 60 В
# # {'Ирина Сапожникова': (25, 160, 60, В)}

from pprint import pprint

group = {}
while s := input():
    l = s.split()
    group[' '.join(l[:2])] = tuple(l[2:])
pprint(group)



# # пример ввода:
    # # Ирина Сапожникова 25 160 60 В
# # {('Ирина Сапожникова', 25, 160, 60, В): True}

group = {}
while s := input():
    group[tuple(s.split())] = True
pprint(group)



# пример ввода:
    # Ирина Сапожникова 25 160 60 В
# {1: {'name': '', 'surname': ''}}

group, i = {}, 1
fields = ('name', 'surname', 'age', 'tall', 'weight', 'grade')
while s := input():
    group[i] = {k: v for k, v in zip(fields, s.split())}
    i += 1
pprint(group)