from pprint import pprint

def map_like(func, sequence):
	return [func(el) for el in sequence]

print(map_like(len, ['a', 'aa', 'a', 'aaaa', 'aa', 'aaa']))
print(map_like(lambda s: s.upper(), ['a', 'aa', 'a', 'aaaa', 'aa', 'aaa']))
