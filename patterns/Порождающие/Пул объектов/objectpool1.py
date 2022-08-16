class ComplexShortUsable:
    def __init__(self, a: int = 0):
        self.a = a
    
    def reset(self):
        self.a = 0


class ObjectsPool:
    def __init__(self, size: int):
        self.store = [ComplexShortUsable() for _ in range(size)]
    
    def get_object(self, a) -> ComplexShortUsable:
        if not self.store:
            self.store += [ComplexShortUsable()]
        obj = self.store.pop()
        obj.a = a
        return obj
    
    def release_object(self, obj) -> None:
        obj.reset()
        self.store += [obj]

