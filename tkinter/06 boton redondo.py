import tkinter as tk

def cambiar():
    label.config(fg=color.get())

root = tk.Tk()

color = tk.StringVar(root, value='black')

for c in ('red', 'green', 'blue'):
    tk.Radiobutton(root, text=c, value=c, variable=color, command=cambiar).pack()

label = tk.Label(root, text='Los alumnos de 2DAM\nson unos profesionales, \nbueno, no todos')
label.pack(pady = 10)

root.mainloop()