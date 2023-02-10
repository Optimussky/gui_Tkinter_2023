# main.py

#This is an app to get a todo list
import tkinter as tk
from customtkinter import CTkLabel
import customtkinter as ctk

"""
import tkinter as tk
import customtkinter as ctk # <- import the CustomTkinter module

root_tk = tk.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("Registro Actividad - App ToDoList")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_tk.mainloop()

"""
#import tkinter
#import customtkinter as ctk

root = tk.Tk()
root.geometry("750x450")
root.title("Listado de Actividades - ToDo App")

title_label = ctk.CTkLabel(root, text="Daly Tasks", text_font=("arial",30))
title_label.pack()


root.mainloop()

