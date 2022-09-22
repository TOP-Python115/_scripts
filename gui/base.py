import tkinter
import tkinter.ttk as ttk


def btn_on_click():
    text_blabel.set(text_field.get())


root = tkinter.Tk()
root.title('Tk Demonstrator')

mainframe = ttk.Frame(root, width=400, height=300, padding=5)
mainframe.grid(row=0, column=0, sticky='nsew')

ttk.Label(
    mainframe,
    text='Введите текст: ',
    font=('Comic Sans MS', 22)
).grid(row=0, column=0, sticky='nw')

text_field = tkinter.StringVar()
ttk.Entry(
    mainframe,
    textvariable=text_field,
    font=('Courier New', 20)
).grid(row=1, column=0, sticky='nwe')

btn = ttk.Button(mainframe, text='\u2193', command=btn_on_click)
btn.grid(row=1, column=1, sticky='nse', padx=(6, 0))

text_blabel = tkinter.StringVar()
ttk.Label(
    mainframe,
    textvariable=text_blabel,
    font=('Courier New', 26, 'bold')  # , background='grey'
).grid(row=2, column=0, columnspan=2, sticky='nsew', pady=5)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(0, weight=1)

root.bind('<Return>', lambda event: btn.invoke())

root.mainloop()
