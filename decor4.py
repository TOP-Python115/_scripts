class Test:
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            print('decorator starts')
            res = func(*args, **kwargs)
            print('decorator ends')
            return res
        return _wrapper
    
    def _decorator_self(func):
        def _wrapper(self):
            print('decorator with self starts')
            res = func(self)
            print('decorator with self ends')
            return res
        return _wrapper
    
    @_decorator
    def test_method(self):
        print('test method')

    @_decorator_self
    def test_method2(self):
        print('test method 2')


t = Test()
t.test_method()
t.test_method2()
