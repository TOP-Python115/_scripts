class User:
    def __init__(self, name):
        self.login = name
        self._password = input()
    
    @property
    def password(self):
        raise Exception('password is wrrite-only field')
    
    @password.setter
    def password(self, value):
        self._password = value


u1 = User('renard')
