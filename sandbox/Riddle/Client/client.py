from tkinter import *

import api

class Window(Frame):

    def __init__(self, master):
        self._raadsel = None

        """ Initialize the frame """
        Frame.__init__(self, master)
        self.grid()
        self.config(background = "Light Blue")
        self.create_widgets()

    def create_widgets(self):
        self.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.header = Label(self,
                            text = 'Raadsels',
                            fg = '#2a9d8f',
                            bg = 'Light Blue',
                            font = ('Helvetica', 30, 'bold'))

        self.header.grid(row=0, column=0, padx=20, pady = (30, 2))

        self.button1 = Button(self, text = 'Ken je deze al?')
        self.button1['command'] = self.button1_pressed
        self.button1.grid(row = 1, column = 0, pady = (30, 2))

        self.text1 = Text(self, height=3, width=60)
        self.text1.grid(row = 2, column = 0)

        self.button2 = Button(self, text='Het antwoord', bg = 'Light Blue')
        self.button2['command'] = self.button2_pressed
        self.button2.grid(row = 3, column = 0, pady = (30, 2))

        self.text2 = Text(self, height = 5, width = 60)
        self.text2.grid(row = 4, column =0)

    def button1_pressed(self):
        self._raadsel = api.get_raadsel()
        self.text1.delete("1.0", "end")
        self.text2.delete("1.0", "end")
        self.text1.insert(END, self._raadsel['q'])

    def button2_pressed(self):
        self.text2.insert(END, self._raadsel['a'])

#-------------------------------------------------------------

root = Tk()
root.title("Riddle client")
root.geometry("500x350")
root.config(background = "Light Blue")

window = Window(root)

root.mainloop()
