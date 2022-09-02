class Memento:
    def __init__(self, balance: int):
        self.balance = balance


class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int):
        # изменение состояния
        self.balance += amount
        # сохранение состояния
        return Memento(self.balance)

    def restore(self, memento: Memento):
        self.balance = memento.balance

    def __str__(self):
        return f'balance: {self.balance}'


ba = BankAccount(100)
print(f'Start. {ba}')

m1 = ba.deposit(50)
m2 = ba.deposit(30)
print(f'Two deposits. {ba}\n')

ba.restore(m1)
print(f'Restore m1. {ba}\n')

ba.restore(m2)
print(f'Restore m2. {ba}\n')
