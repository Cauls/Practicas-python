import tkinter as tk

root = tk.Tk()

def cambiar():
    label.config(text = 'ON')

label = tk.Label(root, text='OFF')
label.pack(pady=20)

boton = tk.Button(root, text='Cambiar', command=cambiar)
boton.pack(pady=20)

root.mainloop()