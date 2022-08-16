
def func(string, splitter=None, start_index=0, end_index=0, trims=''):
	return (string.split(splitter),
		   string[start_index:end_index],
		   string.strip(trims))

print(func('hello! how are you?', trims='?!,', splitter=' ', 
		  start_index=10, end_index=15))
