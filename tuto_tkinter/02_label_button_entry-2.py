import tkinter as tk

num1 = 2
num2 = 2

result = 0
total = result
def suma(num1, num2):
    
    total = num1 + num2
    print(label.cget("text"))
   
    return total



if __name__=='__main__':
    window = tk.Tk()
    window.title("Tkinter First App")
    window.geometry('600x400')

    # Adding Label
    
    inicio = tk.Label(window, text="La suma de 2 + 2 es ")
    label = tk.Label(window, text = total )
    inicio.pack()
    label.pack()

    # Adding Button
    resultBtn = tk.Button(window)
    resultBtn["text"]="Resultado"
    resultBtn["command"]=suma
    resultBtn.pack()


    window.mainloop()