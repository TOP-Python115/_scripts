from abc import ABC, abstractmethod
from enum import Enum


DEBUG = True


class BankAccount:
    """Адресат (receiver) команды."""
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        if DEBUG:
            print(f' -> deposit {amount}')

    def withdraw(self, amount: int):
        if self.balance - amount >= self.__class__.OVERDRAFT_LIMIT:
            self.balance -= amount
            if DEBUG:
                print(f' <- withdraw {amount}')
            return True
        return False

    def __str__(self):
        return f'Balance: {self.balance}'


class Command(ABC):
    """Базовый класс команд."""
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccountCommand(Command):
    """Реализация команды."""
    def __init__(self,
                 account: BankAccount,
                 action: Action,
                 amount: int):
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action is Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        if self.action is Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action is Action.DEPOSIT:
            self.account.withdraw(self.amount)
        if self.action is Action.WITHDRAW:
            self.account.deposit(self.amount)

        self.success = None



acc1 = BankAccount()
print(f'{acc1}\n')

acc1_dep = BankAccountCommand(acc1, Action.DEPOSIT, 100)
acc1_dep.undo()
print(f'{acc1}')
acc1_dep.invoke()
print(f'{acc1}')
acc1_dep.undo()
print(f'{acc1}')
acc1_dep.undo()
print(f'{acc1}\n')

acc1_wdr1 = BankAccountCommand(acc1, Action.WITHDRAW, 50)
acc1_wdr1.invoke()
print(f'{acc1}')
acc1_wdr1.undo()
print(f'{acc1}\n')

acc1_wdr2 = BankAccountCommand(acc1, Action.WITHDRAW, 1000)
acc1_wdr2.invoke()
print(f'{acc1}')
acc1_wdr2.undo()
print(f'{acc1}')
