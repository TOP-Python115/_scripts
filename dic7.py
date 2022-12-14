# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. Поскольку с каждой клавишей связано несколько букв. 
# При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2, 3, 4 или 5 раз заменяет введённый символ на второй, третий, четвертый или пятый символ из определённых для клавиши.
# Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения

# Пример ввода:
# Hello!
# Пример вывода
# 44335555556661111

num_keys = {'1': '.,?!:1',
		'2': 'ABC2',
		'3': 'DEF3',
		'4': 'GHI4',
		'5': 'JKL5',
		'6': 'MNO6',
		'7': 'PQRS7',
		'8': 'TUV8',
		'9': 'WXYZ9',
		'0': ' '}

res = ''
text = input().upper()
for c in text:
	for k, v in num_keys.items():
		res += k * (v.find(c)+1)

print(res)
