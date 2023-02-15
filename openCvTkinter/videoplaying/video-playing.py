"""
A basic video playing option for TKinter GUI windows using openCV
Author 	: Alberto Romero
Date 	: February 2023
install openCV first : pip install opencv-python

Posible tutorial a seguir: GUI con Tkinter y OpenCV en Python | Videos - https://omes-va.com/tkinter-opencv-video/

"""

import cv2
import tkinter as tk
from tkinter import *
#from tkinter import ttk
from tkinter import Frame
#from ttk import Frame
from PIL import Image, ImageTk
#import Image, ImageTk

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 480

#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.resizable(0,0)
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)                

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('camVideo.mp4')

def show_frame():
    try:

        ret, frame = cap.read()

        cv2image   = cv2.cvtColor(ret,frame, cv2.COLOR_BGR2RGBA)

        img   = Image.fromarray(cv2image).resize((760, 400))
        imgtk = ImageTk.PhotoImage(image = img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
    except :
        print(f"Error: ")

closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())              
closeButton.place(x=270,y=430)	

show_frame()  #Display
mainWindow.mainloop()  #Starts GUI