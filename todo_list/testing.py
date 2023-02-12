# https://github.com/TomSchimansky/CustomTkinter/wiki/CTkEntry
import tkinter as tk
import customtkinter as ctk


root = ctk.CTk()  # create the Tk window like you normally do
root.geometry("750x480")
root.title("CustomTkinter Test")


# Add add_todo function
def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0,ctk.END)


# Add Label
titleLabel = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30,weight="bold"))
titleLabel.pack(padx=10, pady=(40,20))

# Add Scroll
scrollable_frame= ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack(fill="x")

# Add Entry
entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add ToDo")
entry.pack()
entry.focus()

# Add Button
add_button = ctk.CTkButton(root, text="Add" , width=500, command=add_todo)
add_button.pack(pady=20)
root.mainloop()
