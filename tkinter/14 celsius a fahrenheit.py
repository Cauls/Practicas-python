import tkinter as tk

root = tk.Tk()
root.title('Conversor de unidades')

def conversion():
    caf = float(e1.get()) * 9/5 + 32
    resultado.config(text= f'{caf}')

tk.Label(root, text='Celsius').grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text='Fahrenheit').grid(row=1, column=0, padx=5, pady=5)

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=5, pady=5)

tk.Button(root, text='Convertir', command=conversion).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

resultado = tk.Label(root, text='')
resultado.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()