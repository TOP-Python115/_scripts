a = int(input('Введите возраст: ' ))

if 1 <= a <= 14:
    print('детство', end='\n\n')
elif 15 < a <= 28:
    print('молодость', end='\n\n')
elif 28 < a <= 65:
    print('зрелость', end='\n\n')
else:
    print('старость')
print('конец')

