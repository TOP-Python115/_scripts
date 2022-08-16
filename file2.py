from sys import argv

for arg in argv[1:]:
	i = arg.rfind('.')
	if i and arg[i+1:] in ('txt', 'py', 'cpp', 'js'):
		with open(arg, encoding='utf-8') as fin:
			print(fin.read(), '\n\n')
