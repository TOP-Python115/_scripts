
l = [1, 2, 3, [1, (9, 8, 7)], (10, 11), range(1, 5, 2)]

def recur_sum(sequence):
	sum = 0
	for el in sequence:
		if isinstance(el, (int, float)):
			sum += el
		elif isinstance(el, (list, tuple, range)):
			sum += recur_sum(el)
		else:
			pass
	return sum


print(recur_sum(l))
