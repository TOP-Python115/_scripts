from pprint import pprint

words = []
while s := input('введите слово: '):
	d = {}
	for c in s:
		# развёрнутая версия – неэффективно
		# if c in d:
		# d[c] = d[c] + 1
		# else:
		# d[c] = 1

		# эффективный вариант
		d[c] = d.get(c, 0) + 1
		words += [d]
		
pprint(words)
	