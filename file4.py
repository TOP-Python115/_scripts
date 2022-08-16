import csv

file_r_path = "d:\\G-Doc\\YandexDisk\\Job\\Компьютерная академия Шаг\\Python web\\_scripts\\file4.csv"


with open(file_r_path, encoding='utf-8') as fin:
	csv_obj = csv.reader(fin)
	
	l = []
	# пропуск заголовка
	csv_obj.__next__()
	for line in csv_obj:
		l += [list(map(lambda x: float(x) if '.' in x else int(x), line))]
	
	print( *l, sep='\n' )
