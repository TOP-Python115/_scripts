from pprint import pprint

try:
    a = b + 1

except NameError as err1:

    try:
        print(err1.name)
        print(err1.args, end='\n\n')
        1 / 0
    
    except Exception as err2:
        print(type(err2))
        print(err2.args, end='\n\n')
        
        err_cont = err2.__context__
        print(type(err_cont))

        for attr in dir(err2.__traceback__):
            print(getattr(err2.__traceback__, attr))
