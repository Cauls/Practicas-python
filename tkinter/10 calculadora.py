import tkinter as tk

def sumar():
    sum = float(e1.get()) + float(e2.get())


root = tk.Tk()
root.title('Calculadora')

e1 = tk.Entry(root).pack()
e2 = tk.Entry(root).pack()
