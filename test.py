import tkinter


class Game:
    def ___init___(self):
        self.window = tkinter.Tk()
        self.c_m = tkinter.Listbox(self.window)
        self.c_m.insert(0, 'вася')
        self.c_m.insert(tkinter.END, 'ася')
        self.c_m.pack()
        tkinter.Button(self.window, x)
        self.window.mainloop()


Game()