"""Сущность Контроллер (MVC)."""

import view
import model


def show_all():
    people = model.Person.get_all()
    view.show_all_view(people)


def start():
    view.start_view()
    inp = view.ask_if_show()
    if inp.lower() == 'д':
        show_all()
    view.end_view()


if __name__ == '__main__':
    start()
