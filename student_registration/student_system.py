# studet_system.py #https://www.youtube.com/watch?v=hUVJv-845FY
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

root = tk.Tk()
root.geometry('500x600')
root.title('Tkinter (Student Management && Registration System)')

bg_color = '#273b7a'
login_student_icon = tk.PhotoImage(file='images/login_student_img.png')

welcome_page_fm = tk.Frame(root,highlightbackground=bg_color,
                           highlightthickness=3)

heading_lb = tk.Label(welcome_page_fm, 
                        text='Welcome To Student \nManagement Registration',
                        bg=bg_color, fg='white', font=('Bold',18))
heading_lb.place(x=0,y=0,width=400)

student_login_btn = tk.Button(welcome_page_fm, text='Login Student', bg=bg_color, 
                            fg='white', font=('Bold',15), bd=0)
student_login_btn.place(x=120, y=125, width=200)


student_login_img = tk.Button(welcome_page_fm, image=login_student_icon, bg=bg_color, bd=0)
student_login_img.place(x=60, y=100)

welcome_page_fm.pack(pady=30)
welcome_page_fm.pack_propagate(False)
welcome_page_fm.configure(width=400,height=420)


root.mainloop()