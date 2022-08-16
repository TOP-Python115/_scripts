
def recur_func(x):
	if x == 0:
		return 0
	else:
		return recur_func(x - 1)


recur_func(5)

# || recur_func(5) /\
# || recur_func(4) ||
# || recur_func(3) ||
# || recur_func(2) ||
# || recur_func(1) ||
# \/ recur_func(0) ||
