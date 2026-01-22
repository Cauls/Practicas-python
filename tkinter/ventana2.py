import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('200x300')
root.title('Hugo es pedofilo')
texto = 'ON'
def saludar():
    messagebox.showinfo('Saludo', '¡Hola mundo!')

boton = tk.Button(root, text='Saludar', command=saludar)
boton.pack(pady=20)

root.mainloop()