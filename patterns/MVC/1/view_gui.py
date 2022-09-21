from time import sleep
from tkinter import Tk, ttk, Text, StringVar
from model import Person

import controller


root = Tk()
root.title('Демонстратор MVC')
root.geometry('400x1075-50+50')

mainframe = ttk.Frame(root, padding=5)
mainframe.grid(sticky='nsew')

message = StringVar()
mainlbl = ttk.Label(mainframe, textvariable=message, font=22)
mainlbl.grid(row=0, column=0, sticky='nsew')

answer = StringVar()
entry = ttk.Entry(mainframe, textvariable=answer, font=22)
entry.grid(row=1, column=0, sticky='nsew')

textfield = Text(mainframe, font=20)
textfield.grid(row=2, column=0, sticky='nsew')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(2, weight=1)


def show_all_view(people: tuple[Person, ...]):
    """Формирует представление, отображающее содержимое базы данных."""
    message.set(f'В базе данных {len(people)} человек.')
    people = '\n'.join(str(p) for p in people)
    textfield.insert('1.0', people)
    root.after(10000, controller.end)


def start_view():
    """Формирует начальное представление."""
    message.set('Приветствую в демонстраторе MVC!')
    root.after(2000, controller.ask_if_show)
    root.mainloop()


def ask_if_show_view():
    """Формирует представление с вопросом, получает пользовательский ввод и передаёт его в контроллер."""
    message.set('Хотите посмотреть содержимое базы данных? [д/н]')
    root.after(5000, controller.yes_or_no, answer.get())


def end_view():
    """Формирует завершающее представление."""
    message.set('Пока!')
    root.after(2000, exit)
