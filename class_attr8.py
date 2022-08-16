class User:
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

User.is_adult(20)

u = User()
# приведёт к ошибке
u.is_adult(15)
# User.is_adult(u, 15)


class Person:
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

Person.is_adult(20)

p = Person()
# корректно
p.is_adult(15)
# Person.is_adult(15)
