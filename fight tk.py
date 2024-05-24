import tkinter

'''
ООП - обьекто обективное програмирование
ООП - стиль програмирования

Класс - фабрика экземпляровб идея
Экземпляр - конкретная реализация объекта

class пишится с заглавной буквы
'''


class Player:
    def __init__(self) -> None:
        self.name = 'игрок'
        self.hр = 100
        self.attack_power = 10
        self.window = tkinter.Tk()
        self.window.mainloop
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.c_m = tkinter.Listbox(self.window)
