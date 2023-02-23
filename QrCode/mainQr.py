# mainQr.py
import tkinter as tk
from tkinter import Button,Label,Entry
import qrcode

root=tk.Tk()
root.title("Generador de QR DDS")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save(str(name)+".png")


Label(root, text="Titulo",fg="white",bg="#AE2321",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

texto=Label(root, text="Introduzca la cadena a convertir en QR",font=15).place(x=50,y=250)
entry=Entry(root,width=28, font="arial 15")
entry.place(x=50,y=290)

Button(root, text="Generar QR", width=20, height=2, bg="black", fg="white", command=generate).place(x=50,y=340)

footer_frame = tk.Frame(root)
designed=Label(footer_frame, text="Designed by ®Alberto Romero™ SSC-DDS February 2023", font=10)

footer_frame.pack(side="bottom", fill="x")
designed.pack(side="right")

root.mainloop()
