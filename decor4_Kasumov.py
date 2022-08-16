from time import perf_counter_ns
# библиотека pathlib полезна и вкусна
from pathlib import Path

# это гарантирует вам прочтение файла на любой платформе
logpath = Path('file.txt')

class Person:
    def __init__(self, name, login, email):
        self.name = name
        self.login = login
        self.email = email

class TxtMsgSender(Person):
    # если наследуете метод без изменений, то нет необходимости его переопределять
    # def __init__(self, name, login, email):
        # super().__init__(name, login, email)
    
    # def decorator_(foo):
        # def magic(self):
            # with open ('file.txt', "w") as file:
                # file.write(f"start: {perf_counter_ns} \n")
                # foo(self)
                # file.write(f"end: {perf_counter_ns}")
        # return magic

    # ⮬ имена для методов, параметров и прочих переменных стоит подобрать получше 
    # предпочтительный вариант реализации декоратора ⮯
    
    # '_' в начале имени указывает на необходимость использования этого имени  
    #   только внутри того пространства имён, где это имя объявлено
    def _elapsetime_logger(func):
        # декоратор может быть применён к методу, принимающему 
        #   произвольное количество аргументов
        def _wrapper(self, *args, **kwargs):
            with open(logpath, "w") as file_handler:
                # perf_counter_ns – это метод
                start = perf_counter_ns()
                # декоратор может быть применён к методу, возвращающему значение
                res = func(self, *args, **kwargs)
                # чтобы точнее засечь время, лучше не совершать никаких 
                #   других действий во время старта и остановки таймера 
                stop = perf_counter_ns()
                file_handler.write(f"Elapse time for {func.__name__}: {stop - start} ns")
                # лучше всегда возвращать это значение, даже если там None
                return res
        return _wrapper

    @_elapsetime_logger
    def message(self):
        print(f"Меня зовут {self.name}. Это мой логин: {self.login} и моя почта: {self.email}")


a = TxtMsgSender("Vusal", "vusalindahouse", "vusi444@gmail.com")
# метод message() не возвращает значения кроме None – печатать нечего
# print(a.message())
a.message()

# stdout:
# Меня зовут Vusal. Это мой логин: vusalindahouse и моя почта: vusi444@gmail.com

# file.txt:
# Elapse time for message: 490000 ns
