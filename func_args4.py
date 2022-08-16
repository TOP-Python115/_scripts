
def av_arith(*args):
	# print(type(args))
	return sum(args) / len(args)

def av_geom(num1, num2):
	return (num1 * num2) ** 0.5

def average(type, *args):
	if type == 'a':
		return sum(args) / len(args)
	if type == 'g':
		prod = 1
		for num in args:
			prod *= num
		return prod**(1/len(args))


print(av_arith(1))
print(av_arith(1, 2))
print(av_arith(1, 2, 3, 4, 5))

