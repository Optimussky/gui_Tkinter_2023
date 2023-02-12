# screen_recorder.py
# URL tuto: https://www.youtube.com/watch?v=lQP0pZ7rCKk&t=144s
# icons https://www.pngwing.com/es/search?q=bot%C3%B3n+Detener
from tkinter import *
import tkinter as tk
import pyscreenrec
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.geometry("400x600")
root.title("Grabador de Pantalla")
root.config(bg="#fff")
root.resizable(False,False)


# Create functions
def start_rec():
    try:

        file=Filename.get()
        rec.start_recording(str(file+".mp4"),5)
    except:
        print("Error en start record")

def pause_rec():
    try:

        rec.pause_recording()
    except:
        print("Error en pausa recording")

def resume_rec():
    try:

        rec.resume_recording()
    except:
        print("Error en resume recording")

def stop_rec():
    try:

        rec.stop_recording()
    except:
        print("Error en stop recording")



# start recording
rec = pyscreenrec.ScreenRecorder()

# data images =  W:234, Height=284 Resolution=72
#icon
image_icon = PhotoImage(file="camera.png")
root.iconphoto(False,image_icon)

# background images
image1 = PhotoImage(file="yellow.png")
Label(root,image=image1,bg="#fff").place(x=-350,y=10)

image2 = PhotoImage(file="blue.png")
Label(root,image=image2, bg="#fff").place(x=223,y=200)

# Heading
head = Label(root,text="Screen Recorder SSC", bg="#fff", font="Arial 15 bold")
head.pack(pady=20)



#Load image
image3 = Image.open('camera.png')
image3=image3.resize((300,200))
image3 = ImageTk.PhotoImage(image3)
Label(root, image=image3,bd=0).pack(pady=150)



# Entry
Filename = StringVar()
entry = Entry(root,textvariable=Filename,width=18,font="Arial 15")
entry.place(x=100, y=345)

Filename.set("Nombre_su_video")
entry.focus()




# Buttons
"""
#Tkinter buttons https://guia-tkinter.readthedocs.io/es/develop/chapters/7-options/7.1-Intro.html
"""

start = Button(root, text="Start", font="Arial 18",bd=0,bg='red',activebackground='#00ff00',cursor="hand2 #FF5733",command=start_rec)
start.place(x=240,y=300)



image4 = Image.open('play.png')
image4=image4.resize((50,50))
image4 = ImageTk.PhotoImage(image4)
resume=Button(root,image=image4,bd=0,bg='#fff',activebackground='green',cursor="hand2 #FF5733",command=resume_rec)
resume.place(x=80,y=450)

image5 = Image.open('pause.png')
image5=image5.resize((50,50))
image5 = ImageTk.PhotoImage(image5)
pause=Button(root,image=image5,bd=0,bg='#fff',activebackground='blue',cursor="hand2 #FF5733",command=pause_rec)
pause.place(x=180,y=450)

image6 = Image.open('stop.png')
image6=image6.resize((50,50))
image6 = ImageTk.PhotoImage(image6)
stop=Button(root,image=image6,bd=0,bg='#fff',activebackground='red',cursor="hand2 #FF5733",command=stop_rec)
stop.place(x=280,y=450)



root.mainloop()
