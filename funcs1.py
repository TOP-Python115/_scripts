# программа на вход получает минуты
# выводит количество часов и минут в формате:
# 2 часа 30 минут
# 5 часов 41 минута

def noun_ending(number, h_or_m=True):
    lld = number % 100
    if lld in (11, 12, 13, 14):
        return 'ов' if h_or_m else ''
    ld = number % 10
    if ld in (0, 5, 6, 7, 8, 9):
        return 'ов' if h_or_m else ''
    elif ld in (2, 3, 4):
        return 'а' if h_or_m else 'ы'
    else:
        return '' if h_or_m else 'а'


while minutes := int(input()):
    h, m = minutes // 60, minutes % 60
    print(f"{h} час{noun_ending(h)} {m} "
           f"минут{noun_ending(m, False)}")
