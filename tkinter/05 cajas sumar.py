import tkinter as tk

def sumar():
    label.config(text = int(num1.get()) + int(num2.get()))

root = tk.Tk()

num1 = tk.Entry(root)
num1.pack()

num2 = tk.Entry(root)
num2.pack()

label = tk.Label(root, text='0')
label.pack()

boton = tk.Button(root, text = 'Sumar', command=sumar)
boton.pack()

root.mainloop()
