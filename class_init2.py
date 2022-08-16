class Test:
    def __init__(self):
        print('__init__ constructor')
        # self.__post_init__()
    
    def __post_init__(self):
        print('__post_init__ method')


t = Test()
