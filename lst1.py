# программа принимает на вход числа, пока не будет введена пустая строка, и добавляет введённые числа в список
# вывести минимальное, среднее и максимальное значения в сформированном списке

l = []
while s := input():
    l += [int(s)]

print(f"min: {min(l)}\nav: {sum(l)/len(l):.2f}\nmax: {max(l)}")
