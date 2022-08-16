
def func(pos_arg1, pos_arg2, *args, kw_arg1=0, kw_arg2='', **kwargs):
	print(pos_arg1, pos_arg2, 
		 *args, 
		 kw_arg1, kw_arg2,
		 *kwargs.values(),
		 sep='\n')


