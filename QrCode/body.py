# mainQr.py
import tkinter as tk
from tkinter import Button,Label,Entry,PhotoImage
import qrcode
from mainQr2 import generador_qr


root=tk.Tk()
root.title("Generador de QR DDS")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)


# Create Label and add some text
Upper_right = tk.Label(root,text ='DDS SSC-CDMX')
 
# using place method we can set the position of label
Upper_right.place(relx = 0.0,
                  rely = 0.0,
                  anchor ='nw')


"""
# Algo de teoría:
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


###start function####
def generate_png():
    name=title.get()
    text=entry.get()
    print(name + " Título " + text + " Texto")
    qr=qrcode.make(text)
    qr.save(str(name)+".png")

def png():
    print("Formato PNG")

def jpg():
    print("Formato JPG")

def svg():
    print("Formato SVG")

def pdf():
    print("Formato PDF")

x_png=png()
x_jpg=jpg()
x_svg=svg()
x_pdf=pdf()

todo = [x_png,x_jpg,x_svg,x_pdf]
def all_formats(*todo):
    #f_png= png()
    #f_jpg=jpg()
    #f_svg=svg() 
    #f_pdf=pdf()

    return x_png,x_jpg,x_svg,x_pdf   


####end function###


"""

history = generador_qr()


Label(root, text="Título",fg="white",bg="#AE2321",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)
title.focus()
texto=Label(root, text="Introduzca la cadena a convertir en QR",font=15).place(x=50,y=250)
entry=Entry(root,width=28, font="arial 15")
entry.place(x=50,y=290)


Button(root, text="Generar QR", width=20, height=2, bg="black", fg="white", command=history).place(x=50,y=340)

footer_frame = tk.Frame(root)
designed=Label(footer_frame, text="Designed by ®Alberto Romero™ SSC-DDS February 2023", font=10)

footer_frame.pack(side="bottom", fill="x")
designed.pack(side="right")

icono = tk.PhotoImage(file="ico.png")
# Establecerlo como ícono de la ventana.
back_ground_pic=PhotoImage(file='ssc.jpg')
Label(root,image=back_ground_pic,bg='grey').pack(side='right')
root.wm_attributes("-transparentcolor", 'grey')

root.iconphoto(True, icono)

root.mainloop()
