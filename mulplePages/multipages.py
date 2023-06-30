import tkinter as tk
from tkinter import Frame, Button, Label, BOTH, LEFT, RIGHT, BOTTOM
root = tk.Tk()
root.geometry('300x400')
root.title('Switching pages')

main_frame = Frame(root)
bottom_frame = Frame(root)

page_1 = Frame(main_frame)
page_1_lb = Label(page_1, text='Start Page', font=('Bold', 20))
page_1_lb.pack()


page_1_lb.pack(pady=100)

page_2 = Frame(main_frame)
page_2_lb = Label(page_1, text='Home', font=('Bold', 20))
page_2_lb.pack()


page_3 = Frame(main_frame)
page_3_lb = Label(page_1, text='Menu', font=('Bold', 20))
page_3_lb.pack()


page_4 = Frame(main_frame)
page_4_lb = Label(page_1, text='About', font=('Bold', 20))
page_4_lb.pack()


pages = [page_1,page_2,page_3,page_4]
count = 0


def move_next_page():
    global count

    if not count > len(pages) -2:
        
        for p in pages:
            p.pack_forget()
        
        count += 1
        page = pages[count]
        page.pack(pady=100)




main_frame.pack(fill=BOTH, expand=True)



back_btn = Button(bottom_frame,text='Back', font=('Bold',12), bg='#1877f2', fg='white',width=8)
back_btn.pack(side=LEFT, padx=10)

next_btn = Button(bottom_frame, text='Next', font=('Bold', 12),bg='#1877f2',fg='white',width=8, command=move_next_page)
next_btn.pack(side=RIGHT, padx=10)

bottom_frame.pack(side=BOTTOM, pady=10)


root.mainloop()