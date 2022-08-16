# программа принимает на вход числа в одну строку, разделённые пробелами

l = input().split()

for i in range(len(l)):
    l[i] = int(l[i])

print(sum(l), '\n')

for el in l:
    print(f"{el}\t{'div 3' if el % 3 == 0 else 'not'}")
