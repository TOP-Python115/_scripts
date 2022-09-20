"""Сущность Контроллер (MVC)."""

import view
import model


def show_all():
    """Запрашивает данные из Модели и передаёт их в Представление."""
    people = model.Person.get_all()
    view.show_all_view(people)


def start():
    """Выполняет последовательность работы приложения."""
    # 1. Начальное представление
    view.start_view()
    # 2. Представление с вопросом, передающее введённый ответ пользователя
    inp = view.ask_if_show()
    # 3. Обработка введённого ответа
    if inp.lower() == 'д':
        show_all()
    # 4. Завершающее представление
    view.end_view()


if __name__ == '__main__':
    start()
