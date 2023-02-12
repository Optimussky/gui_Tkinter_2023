# 01_basic_tk_app.py

def hello():
    print("Hello world")

import tkinter as tk

window=tk.Tk()
button=tk.Button(window, text='Hello world',command=hello)
button.pack()
window.mainloop()
