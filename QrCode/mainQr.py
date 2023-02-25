# mainQr.py
import os
from os import system
import tkinter as tk
from tkinter import Button,Label,Entry,messagebox
import qrcode


root=tk.Tk()
root.title("Generador de QR DDS")
root.geometry("1000x550")
root.config(bg="#75293d")#75293d ,#AE2321
root.resizable(False,False)

def open_Qr_dir():
    os.system('explorer .')
def success_msg():
    title_msg = "Gracias por usar la App."
    success_msg = "¡Código Qr generado con éxito!"
    messagebox.showinfo(title_msg,success_msg) 

def clear_entry():
    title.delete(0,'end')
    my_qr.delete(0,'end')

def generate_png():
    name=title.get()
    text=my_qr.get()
    print(name + " Título " + text + " Texto")
    qr=qrcode.make(text)
    qr.save(str(name)+".png")
    clear_entry()
    success_msg()
    open_Qr_dir()
    

# Create Label and add some text
Upper_right = tk.Label(root,text ='DDS SSC-CDMX', bg='#a88b5b')
 
# using place method we can set the position of label
Upper_right.place(relx = 1.0,
                  rely = 0.0,
                  anchor ='ne')



Label(root, text="Título",fg="white",bg="#a88b5b",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)
title.focus()
texto=Label(root, text="Introduzca la cadena a convertir en QR",fg="white",bg='#a88b5b',font=15).place(x=50,y=250)
my_qr=Entry(root,width=28, font="arial 15")
my_qr.place(x=50,y=290)


Button(root, text="Generar QR", width=20, height=2,font ='bold', bg="#d6ad28", fg="white", command=generate_png).place(x=50,y=340)

footer_frame = tk.Frame(root)
designed=Label(footer_frame, text="Designed by ®Alberto Romero™ SSC-DDS February 2023", font=10 ,bg='#888b8d', fg='#d6ad28')

footer_frame.pack(side="bottom", fill="x")
designed.pack(side="right")

root.mainloop()
