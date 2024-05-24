import tkinter
import random
import time
from questions5 import questions


class App:
    '''Приложение'''
    def __init__(self, shuffle_questions=False, shuffle_answers=False) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 30))
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.main_frame = tkinter.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        self.start_time = 0
        self.end_time = 0
        self.time_total = 0
        self.shuffle_questions = shuffle_questions
        self.shuffle_answer = shuffle_answers
        self.start()
        self.window.mainloop()

    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def start(self) -> None:
        self.start_time = time.time()
        self.clear()
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
        self.show_question()

    def show_question(self) -> None:
        question = questions[self.quiestion_index]
        if self.shuffle_answer:
            tkinter.Label(self.main_frame, text='тема:').pack()
            tkinter.Label(self.main_frame, text=question['теги']).pack()
            tkinter.Label(self.main_frame, text='').pack()
            random.shuffle(question['ответы'])
        tkinter.Label(
            self.main_frame,
            text=f'{self.quiestion_index}/{len(questions)}'
        ).pack()
        image_file = question.get('картинка')
        if image_file:
            photo_image = tkinter.PhotoImage(file=question['картинка'])
            tkinter.Label(self.main_frame, image=photo_image).pack()

        tkinter.Label(self.main_frame, text=question['вопрос']).pack()
        buttons_frame = tkinter.Frame(self.main_frame)
        buttons_frame.pack()
        for answer in question['ответы']:
            tkinter.Button(
                buttons_frame,
                text=answer,
                command=lambda arg=answer: self.on_button(arg),
            ).pack(side='left', padx=25, pady=25, ipadx=25, ipady=15)

    def on_button(self, button_text) -> None:
        self.clear()
        question = questions[self.quiestion_index]
        if button_text == question['индекс правильного ответа']:
            self.right_anwers += 1
        else:
            self.wrong_anwers += 1

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.quiestion_index += 1
        if self.quiestion_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self) -> None:
        '''Показывает результат викторины'''
        self.end_time = time.time()
        self.time_total = self.end_time - self.start_time + 100
        hours = self.time_total // 3600
        minutes = self.time_total // 60 % 60
        seconds = round(self.time_total % 60)
        tkinter.Label(self.main_frame,
                      text='Викторина завершена!').pack(pady=(25, 0))
        tkinter.Label(self.main_frame,
                      text=f'время: {hours:02} / {minutes:02} / {seconds:02}'
                      ).pack(pady=(15, 0))
        tkinter.Label(self.main_frame,
                      text=f'Всего вопросов: {len(questions)}'
                      ).pack(pady=(15, 0))
        tkinter.Label(self.main_frame,
                      text=f'Правильных ответов: {self.right_anwers}'
                      ).pack(pady=(15, 0))
        tkinter.Label(self.main_frame,
                      text=f'Ошибок: {self.wrong_anwers}').pack(pady=(15, 0))
        tkinter.Button(self.main_frame, text='начать заново',
                       command=self.start).pack(pady=(25, 0))


App(shuffle_questions=True, shuffle_answers=True)
