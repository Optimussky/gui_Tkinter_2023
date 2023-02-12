# 01_mainloop.py

import tkinter as tk



def hello():
    print("Hello World")


if __name__=='__main__':
    # Addng root
    window=tk.Tk()
    window.title("Tkinter Title")
    window.geometry("600x400")

    # Adding Frame
    frame = tk.Frame(window)
    frame.pack()

    # Adding Label
    label = tk.Label(frame, text="Hello Wordl")
    label.pack()
    #Print the origin widget(path Label)
    print(str(label))

    # Adding Button
    button = tk.Button(frame, text='Click Button', command=hello)
    button.pack()
    # Print the origin widget(path Button)
    print(str(button))

    # Adding loop
    window.mainloop()

    print("Este texto se imprime al cerrar la App, ya qu esta al final del mainloop")
