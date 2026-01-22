import tkinter as tk

contador = 0

def sumar():
    global contador
    contador+=1
    label.config(text=contador)

def restar():
    global contador
    contador-=1
    label.config(text=contador)

root = tk.Tk()
root.geometry('300x300')
label = tk.Label(root, text=contador, font=('Arial', 20))
label.pack()

botonSumar = tk.Button(root, text='+1', command=sumar)
botonRestar = tk.Button(root, text='-1', command=restar)

botonSumar.pack(pady=20)
botonRestar.pack(pady=20)

root.mainloop()