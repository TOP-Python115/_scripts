# 'r' чтение 
# 'w' перезапись
# 'a' дозапись

file_path = r'd:\G-Doc\YandexDisk\Job\Компьютерная академия Шаг\Python web\115\scripts\zip2.py'

# открыть файл в текстовом режиме (вариант по умолчанию) для чтения
with open(file_path, 'rt') as f_in:
	pass


# открыть файл в текстовом режиме для чтения
with open(file_path, 'rt', encoding='utf-8') as f_in:
	lines = f_in.readlines()
	for i in range(len(lines)):
		print(f'{i+1}:\t{lines[i]}')


# открыть файл в текстовом режиме для записи в конец файла
with open(file_path, 'a') as f_in:
	f_in.write('\n\n# appended line')


