from pprint import pprint

e1 = Exception()
e2 = Exception('error message')

# pprint(dir(e1))

try:
    a = b + 1

except NameError as err1:
    pprint(dir(err1))
    print(err1.name)
    print(err1.args)

    for attr in dir(err1.__traceback__):
        print(getattr(err1.__traceback__, attr))
