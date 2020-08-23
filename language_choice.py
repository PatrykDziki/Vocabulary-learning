from tkinter import *

class Language:
    def __init__(self, master):
        self.master = master
        master.title('Wybierz język')
        master.geometry('250x100')
        self.choosen_language = ''

        self.button_1 = Button(master, text='angielski -> polski', command=self.english)
        self.button_1.pack(fill=BOTH, expand=YES)

        self.button_2 = Button(master, text='polski -> angielski', command=self.polish)
        self.button_2.pack(fill=BOTH, expand=YES)

    def english(self):
        self.choosen_language = 'angielski'
        self.master.destroy()

    def polish(self):
        self.choosen_language = 'polski'
        self.master.destroy()
