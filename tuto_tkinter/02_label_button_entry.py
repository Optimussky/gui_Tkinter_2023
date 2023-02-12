import tkinter as tk



if __name__=='__main__':
    window = tk.Tk()
    window.title("Tkinter First App")
    window.geometry('600x400')

    # Adding Label
    
    
    label = tk.Label(window, text = "Hello World")
    label["bg"]="#DEB887" # Colores: https://www.cdmon.com/es/apps/tabla-colores
    label["fg"]="blue"
    label["width"]=50#3 o 50 o x Cantidad de caracteres
    label.pack()
    textEntry = tk.Entry(window,bg="#FFF8DC")
    textEntry.pack(fill='x', padx=10, pady=20)
    textEntry.focus()
    button = tk.Button(window, text='Clic Here',activebackground="#556B2F", activeforeground="white")
    button.pack()

    textEntryDisabled = tk.Entry(window,bg="#FFF8DC",state=tk.DISABLED)
    
    textEntryDisabled.pack(fill='x', padx=10, pady=20)
    buttonDisabled = tk.Button(window, text='Button Disabled',activebackground="#556B2F", activeforeground="white",state=tk.DISABLED)
    buttonDisabled.pack()

    # Adding Button
    #resultBtn = tk.Button(window)
    #resultBtn.pack()
    textEntry.insert(0, "Entry Enabled")
    textEntryDisabled.insert(0, "Entry Disabled")
    window.mainloop()