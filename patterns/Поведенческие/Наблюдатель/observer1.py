class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str):
    print(f'{name} нуждается в докторе по адресу {address}')


ivan = Person('Иван Петров', 'пр. Космонавтов 30')

# подписка на события
ivan.falls_ill.append(
    lambda name, address: print(f'{name} заболел')
)
ivan.falls_ill.append(call_doctor)

# генерация события из клиента
ivan.catch_cold()
