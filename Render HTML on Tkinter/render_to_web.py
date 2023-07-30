#render_to_web.py
"""
Script que pretende renderizar HTML desde python
"""

import tkinter as tk
from tkinterweb import HtmlFrame as hf

screen = tk.Tk()
screen.geometry("700x700")
frame = hf(screen, horizontal_scrollbar="auto")
urlInput = tk.Entry(screen)


def search():
    frame.load_website(urlInput.get())


button = tk.Button(screen, text ="Search", command=search)
frame = hf(screen)
urlInput.grid(row=0, column=0, columnspan=2)
button.grid(row=1, column=0)
frame.grid(row=2, column=0)
screen.mainloop()
