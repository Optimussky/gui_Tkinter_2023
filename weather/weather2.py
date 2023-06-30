# URL https://www.youtube.com/watch?v=NCCYWIzN6hU
import os
import sys
import platform
import subprocess
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Weather App")
root.geometry("980x500+300+200")
root.resizable(False,False)


# Command Functions
def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExcercises")
    localtion = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=localtion.latitude,lat=localtion.latitude)
    #home=pytz.timezone(result)
    local_time = datetime.now()
    now = datetime.now()
    year = now.year
    mes = now.month
    dia = now.day
    hora = now.hour
    minuto = now.minute

    if minuto < 10:
        minutos = f"0{minuto}"
    else:
        minutos = minuto

    current_time = f"{year}-{mes}-{dia} {hora}:{minutos}"
    # Clock and Name
    clock.config(text=current_time)
    name.config(text="Fecha Actual")

    # Weather
    if platform.system() == 'Windows':

        ip = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a \
                                    in ('ping -n 1 -4 "%computername%"') do @echo %a""")
        comando = "Elegiste IP"
        # Print data
        t.config(text=(ip))
        c.config(text=(comando,ip,"Ok"))
    else:
        ip = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    #print(local)


    




# Search box
search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20,y=20)

# Text Entry
textfield = tk.Entry(root, justify="center",  width=46, \
                    font=("poppins",25, "bold"),bg="#404040",border=0,fg="white")
textfield.place(x=60,y=27)
textfield.focus()

# Search icon and Button
search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=25,y=30)

# Logo
# Load the image
logo_image=Image.open('logo_img.png')

# Resize the image in the given (width, height)
logo_image=logo_image.resize((250, 225))
logo_image = ImageTk.PhotoImage(logo_image)
logo = Label(image=logo_image)
logo.place(x=200,y=150)

# Bottom box
# Load the image
frame_image=Image.open('./uno/box.png')

# Resize the image in the given (width, height)
frame_image=frame_image.resize((800, 100))
frame_image = ImageTk.PhotoImage(frame_image)
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5,pady=10,side=BOTTOM)

# Time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


# Label
label1 = Label(root, text="WIND",font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1 = Label(root, text="WIND",font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1 = Label(root, text="WIND",font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1 = Label(root, text="WIND",font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)


# Label place
t=Label(font=("arial",50,"bold"),fg='#00e8fc')
t.place(x=500,y=150)

c=Label(font=("arial",15,"bold"))
c.place(x=500,y=250)


w=Label(text="...",font=("arial",20,"bold"),fg="#545863",bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),fg="#545863",bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),fg="#545863",bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),fg="#545863",bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()