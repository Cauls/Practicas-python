import tkinter as tk

def limpiar():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    resultado.config(text = '')

root = tk.Tk()
root.title('Limpiar campos')

tk.Label(root, text='Numero 1').pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text='Numero 2').pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text='Limpiar', command=limpiar).pack()

resultado = tk.Label(root, text='No limpiado')
resultado.pack()

root.mainloop()