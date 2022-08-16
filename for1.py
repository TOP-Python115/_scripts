DEBUG = True

n, m = int(input()), int(input())
for i in range(n, m):
    if DEBUG:
        print(f'Начинается {i-n+1} итерация внешнего цикла\ni = {i}')
    for k in range(2, i//2):
        if DEBUG:
            print(f'\tНачинается {k-1} итерация внутреннего цикла\n\tk = {k}')
        if i % k == 0:
            if DEBUG:
                print(f'\tнайден делитель! прерывание цикла')
            break
    else:
        print('\t', i)
    if DEBUG:
        print()
