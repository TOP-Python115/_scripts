
def func(**kwargs):
	print(type(kwargs))
	for k in kwargs:
		print(f"key: {k}\tvalue: {kwargs[k]}")
