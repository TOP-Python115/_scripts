import re


class CharacterState:
    """Хранение меняющихся параметров персонажа.

    Хранитель / снимок (memento).
    """
    def __init__(self,
                 health: int,
                 level: int,
                 inventory: list[str],
                 position: dict[str, int]):
        self.health = health
        self.level = level
        self.inventory = inventory
        self.position = position

    def __str__(self):
        return (
            f'H{self.health}, '
            f'Lvl{self.level}, '
            f'x={self.position["x"]}, y={self.position["y"]}'
        )


class Character:
    """Персонаж аркадной игры.

    Создатель (originator).
    """
    def __init__(self, name: str):
        self.name: str = name
        self.health: int = 10
        self.level: int = 1
        self.inventory: list[str] = []
        self.position: dict[str, int] = {'x': 0, 'y': 0}

    def hit(self):
        self.health -= 1

    def progress(self):
        self.level += 1

    def get_item(self, item: str):
        self.inventory += [item]

    def move(self, x: int = 1, y: int = 1):
        self.position['x'] += x
        self.position['y'] += y

    @property
    def state(self) -> CharacterState:
        return CharacterState(
            self.health,
            self.level,
            self.inventory,
            self.position
        )

    @state.setter
    def state(self, char_state: CharacterState):
        self.health = char_state.health
        self.level = char_state.level
        self.inventory = char_state.inventory
        self.position = char_state.position

    def __str__(self):
        return (
            f'{self.name}: '
            f'Hits{self.health}, '
            f'Lvl{self.level}, '
            f'x={self.position["x"]}, y={self.position["y"]}'
        )


class SaveLoadMenu:
    """Предоставляет интерфейс для работы с состояниями персонажа.

    Опекун (caretaker).
    """
    def __init__(self, originator):
        self.originator = originator
        self.__mementos: list = []

    def save(self):
        """Сохраняет состояние объекта Создателя."""
        self.__mementos += [self.originator.state]

    def load(self):
        """Восстанавливает сохранённое ранее состояние объекта Создателя."""
        index = self.show_saves()
        if 0 <= index < len(self.__mementos):
            self.originator.state = self.__mementos[index]
        else:
            raise ValueError

    def show_saves(self, get_index: bool = True) -> int:
        """Выводит все сохранённые состояния объекта Создателя и запрашивает номер необходимого состояния."""
        print('Сохранения:')
        for i, save in enumerate(self.__mementos, 1):
            print(f'\t{i}. {self.originator.name}. {save}')
        while get_index:
            i = input(' номер сохранения > ')
            if re.match(r'\d{1,2}', i):
                return int(i) - 1
            print('...номер — это число...')



hero = Character('Корвин')
menu = SaveLoadMenu(hero)
print(f'Старт.\n{hero}\n')

hero.move(5, 3)
hero.hit()
hero.hit()
hero.progress()
hero.get_item('пистолет')
hero.move(-2, -1)
print(f'Акт 1.\n{hero}\n')

print('Сохранение...\n')
menu.save()

hero.move(1, 6)
hero.hit()
hero.hit()
hero.hit()
hero.get_item('ключ')
print(f'Акт 2.\n{hero}\n')

print('Сохранение...\n')
menu.save()

menu.load()
print(f'...загрузка завершена.\n{hero}\n')

