import tkinter as tk

root = tk.Tk()
root.title('calculadora basica')

def sumar():
    num1 = float(e1.get())
    num2 = float(e2.get())
    resultadosum = num1 + num2
    resultado.config(text = f'Resultado: {resultadosum}')

tk.Label(root, text='Numero1').grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text='Numero2').grid(row=1, column=0, padx=10, pady=5, sticky='e')

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)

e2 = tk.Entry(root)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text='Sumar', command=sumar).grid(row=2, column=0, columnspan=2, pady=10)

resultado = tk.Label(root, text='Resultado')
resultado.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()