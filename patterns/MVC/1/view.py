"""Сущность Представление (MVC)."""

from model import Person


def show_all_view(people: tuple[Person, ...]):
    print(f'В базе данных {len(people)} человек.')
    for pers in people:
        print(pers)


def start_view():
    print(f'Приветствую в демонстраторе MVC!')


def ask_if_show():
    return input('Хотите посмотреть содержимое базы данных? [д/н]\n')


def end_view():
    print(f'Пока!')
