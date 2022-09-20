from time import sleep
from tkinter import Tk, ttk, Text, StringVar
from model import Person

root = Tk()

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky='nsew')

mainlbl = ttk.Label(mainframe)
mainlbl.grid(row=0, column=0, sticky='nsew')

answer = StringVar()
entry = ttk.Entry(mainframe, textvariable=answer)
entry.grid(row=1, column=0, sticky='nsew')

textfield = Text(mainframe)
textfield.grid(row=2, column=0, sticky='nsew')

mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(0, weight=1)


def show_all_view(people: tuple[Person, ...]):
    """Формирует представление, отображающее содержимое базы данных."""
    mainlbl['text'] = f'В базе данных {len(people)} человек.'
    people = '\n'.join(str(p) for p in people)
    textfield.insert('1.0', people)


def start_view():
    """Формирует начальное представление."""
    mainlbl['text'] = 'Приветствую в демонстраторе MVC!'
    root.mainloop()
    sleep(5)


def ask_if_show() -> str:
    """Формирует представление с вопросом, получает пользовательский ввод и передаёт его в контроллер."""
    mainlbl['text'] = 'Хотите посмотреть содержимое базы данных? [д/н]'
    root.update_idletasks()
    sleep(5)
    return answer.get()


def end_view():
    """Формирует завершающее представление."""
    mainlbl['text'] = 'Пока!'
    root.update_idletasks()
    sleep(5)
    exit()
