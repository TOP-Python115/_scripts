"""Сущность Представление (MVC)."""
from time import sleep
from model import Person

import controller


def show_all_view(people: tuple[Person, ...]):
    """Формирует представление, отображающее содержимое базы данных."""
    print(f'В базе данных {len(people)} человек.')
    for pers in people:
        print(pers)
    sleep(10)
    controller.end()


def start_view():
    """Формирует начальное представление."""
    print(f'Приветствую в демонстраторе MVC!')
    sleep(2)
    controller.ask_if_show()


def ask_if_show_view() -> str:
    """Формирует представление с вопросом, получает пользовательский ввод и передаёт его в контроллер."""
    return input('Хотите посмотреть содержимое базы данных? [д/н]\n')


def end_view():
    """Формирует завершающее представление."""
    print(f'Пока!')
    sleep(2)
