
# 5! = 1 * 2 * 3 * 4 * 5
# 5! = 4! * 5
# 4! = 3! * 4
# 3! = 2! * 3
# 2! = 1! * 2
# 1! = 1

def recur_factorial(x):
	if x == 1:
		return 1
	else:
		return recur_factorial(x - 1) * x


while n := int(input()):
	print(recur_factorial(n))

# для выполнения файла – закомментировать до конца
# def recur_factorial(3):
	# if 3 == 1:
		# return 1
	# else:
		# return recur_factorial(3 - 1) * 3

	# def recur_factorial(2):
		# if 2 == 1:
			# return 1
		# else:
			# return recur_factorial(2 - 1) * 2
	
		# def recur_factorial(1):
			# if 1 == 1:
				# return 1
			# else:
				# return recur_factorial(x - 1) * x

	# def recur_factorial(2):
		# if 2 == 1:
			# return 1
		# else:
			# return 1 * 2

# def recur_factorial(3):
	# if 3 == 1:
		# return 1
	# else:
		# return 2 * 3
