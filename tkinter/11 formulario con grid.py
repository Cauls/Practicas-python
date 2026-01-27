import tkinter as tk

root = tk.Tk()
root.title('Formulario con grid')

tk.Label(root, text='Nombre').grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text='Edad').grid(row=1, column=0, padx=10, pady=5, sticky='e')

nombre = tk.Entry(root)
nombre.grid(row=0, column=1, padx=10, pady=5)

edad = tk.Entry(root)
edad.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text='Enviar').grid(row=2, columnspan=2, pady=10)

root.mainloop()