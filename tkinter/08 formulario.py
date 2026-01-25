import tkinter as tk

def guardar():
    texto = f'Nombre : {nombre.get()} | Edad: {edad.get()}'
    resultado.config(text=texto)

root = tk.Tk()

tk.Label(root, text='Nombre').pack()
nombre = tk.Entry(root)
nombre.pack()

tk.Label(root, text='edad').pack()
edad = tk.Entry(root)
edad.pack()

tk.Button(root, text='Guardar', command=guardar).pack()


resultado = tk.Label(root, text='')
resultado.pack()

root.mainloop()

