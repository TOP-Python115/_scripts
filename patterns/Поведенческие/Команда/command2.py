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
    def __init__(self):
        self.success = None

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BACommand(Command):
    """Реализация команды."""
    def __init__(self,
                 account: BankAccount,
                 action: Action,
                 amount: int):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

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


class CompositeBACommand(Command, list):
    """Компоновщик нескольких команд."""
    def __init__(self,
                 command1: BACommand,
                 *commands: BACommand):
        super().__init__()
        commands = (command1, ) + commands
        for command in commands:
            self.append(command)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in reversed(self):
            command.undo()


class MoneyTransfer(CompositeBACommand):
    """Компоновщик для нескольких команд с проверкой успеха выполнения каждой из команд."""
    def __init__(self,
                 from_account: BankAccount,
                 to_account: BankAccount,
                 amount: int):
        super().__init__(
            BACommand(from_account, Action.WITHDRAW, amount),
            BACommand(to_account, Action.DEPOSIT, amount)
        )

    def invoke(self):
        ok = True
        for command in self:
            if ok:
                command.invoke()
                ok = command.success
            else:
                command.success = ok
        self.success = ok


acc1 = BankAccount(100)
acc2 = BankAccount(0)
print(f'acc1 {acc1}\nacc2 {acc2}\n')

amount_to_transfer = 1000
# transfer = CompositeBACommand(
#     BACommand(acc1, Action.WITHDRAW, amount_to_transfer),
#     BACommand(acc2, Action.DEPOSIT, amount_to_transfer)
# )
transfer = MoneyTransfer(acc1, acc2, amount_to_transfer)
transfer.invoke()
print(f'acc1 {acc1}\nacc2 {acc2}\n'
      f'transfer {transfer.success}\n')
transfer.undo()
print(f'acc1 {acc1}\nacc2 {acc2}\n'
      f'transfer {transfer.success}\n')
