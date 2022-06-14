import tkinter as tk
from tkinter import messagebox

def hello():
     messagebox.showinfo("Say Hello", "Hello World")

# def hello():
#      print('Hello')

top = tk.Tk()

btn1 = tk.Button(top, text = "Say Hello", command = hello)
btn1.pack()

top.mainloop()


