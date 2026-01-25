import tkinter as tk

def mostrar():
    label.config(text=entrada.get())

root = tk.Tk()

entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text='Mostrar', command=mostrar)
boton.pack()

label = tk.Label(root, text = '')
label.pack()

root.mainloop()