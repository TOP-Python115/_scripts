from typing import Optional

class Memento:
    def __init__(self, balance: int):
        self.balance = balance


class BankAccount:
    def __init__(self, start_balance: int = 0):
        self.balance = start_balance
        self.changes: list[Memento] = [Memento(start_balance)]
        self._index = 0

    def deposit(self, amount: int) -> Memento:
        """Изменяет состояние экземпляра и запоминает изменённое состояние."""
        self.balance += amount
        m = Memento(self.balance)
        self.changes += [m]
        self._index += 1
        return m

    def undo(self) -> Optional[Memento]:
        """Возврат к предыдущему состоянию."""
        if self._index:
            self._index -= 1
            memento = self.changes[self._index]
            self.balance = memento.balance
            return memento
        return None

    def redo(self) -> Optional[Memento]:
        """Возврат к следующему состоянию."""
        if not self.is_last():
            self._index += 1
            memento = self.changes[self._index]
            self.balance = memento.balance
            return memento
        return None

    def is_last(self) -> bool:
        return True if self._index == len(self.changes) - 1 else False

    def __str__(self):
        return f'balance: {self.balance}'


ba = BankAccount(1000)
print(f'{ba}')

ba.deposit(2500)
ba.deposit(250)
print(f'{ba}\n')

ba.undo()
print(f'Undo 1 — {ba}')
ba.undo()
print(f'Undo 2 — {ba}\n')

ba.redo()
print(f'Redo 1 — {ba}')
ba.redo()
print(f'Redo 2 — {ba}\n')

print(f'{ba.is_last() = }')
