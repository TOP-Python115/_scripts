# Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра. 
# В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None. 
# Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».

def three_args(*, var1, var2=None, var3=None):
    print(f"Переданы аргументы: {var1 = }", end='')
    if var2 is not None:
        print(f", {var2 = }", end='')
    if var3 is not None:
        print(f", {var3 = }", end='')
    print()
