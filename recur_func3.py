
# 1 1 2 3 5 8 13 21 34 55 89 144 
# fibbonacci(100, []) -> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def fibbonacci(limit, initial):
	n1, n2 = initial[-1], initial[-2]
	if n1 + n2 > limit:
		return initial
	else:
		initial += [n1 + n2]
		return fibbonacci(n, initial)


while n := int(input()):
	print(*fibbonacci(n, [1, 1]))


# def fibbonacci(3, [1, 1]):
	# n1, n2 = 1, 1
	# if 1 + 1 > 3:
		# return [1, 1]
	# else:
		# [1, 1] += [1 + 1]
		# return fibbonacci(3, [1, 1, 2])

	# def fibbonacci(3, [1, 1, 2]):
		# n1, n2 = 2, 1
		# if 2 + 1 > 3:
			# return [1, 1, 2]
		# else:
			# [1, 1, 2] += [2 + 1]
			# return fibbonacci(3, [1, 1, 2, 3])

		# def fibbonacci(3, [1, 1, 2, 3]):
			# n1, n2 = 3, 2
			# if 3 + 2 > 3:
				# return [1, 1, 2, 3]
			# else:
				# initial += [n1 + n2]
				# return fibbonacci(n, initial)
