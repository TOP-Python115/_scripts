# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером: 1-111-111-1111.

flag = True

while s := input():
    l = s.split('-')

    if [len(p) for p in l] != [1, 3, 3, 4]:
        flag = False

    if not ''.join(l).isdigit():
        flag = False

    print('correct' if flag else 'incorrect')
    flag = True
