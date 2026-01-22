import tkinter as tk

root = tk.Tk()
root.title('Mi app')
root.geometry('300x200')

tk.Label(root, text='Hola').pack()

root.mainloop()