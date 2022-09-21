"""Сущность Контроллер (MVC)."""

import view
# import view_gui as view
import model


def show_all():
    """Запрашивает данные из Модели и передаёт их в Представление."""
    people = model.Person.get_all()
    view.show_all_view(people)


def start():
    """Выполняет последовательность работы приложения."""
    # 1. Начальное представление
    view.start_view()


def ask_if_show():
    # 2. Представление с вопросом, передающее введённый ответ пользователя
    inp = view.ask_if_show_view()
    if inp:
        yes_or_no(inp)


def yes_or_no(inp: str):
    # 3. Обработка введённого ответа
    if inp.lower() == 'д':
        show_all()


def end():
    # 4. Завершающее представление
    view.end_view()


if __name__ == '__main__':
    start()
