import tkinter as tk

def seleccionar(event):
    label.config(text=listbox.get(listbox.curselection()))

root = tk.Tk()

listbox = tk.Listbox(root)
for ciudad in ['Madrid', 'Sevilla', 'Valencia', 'Bilbao']:
    listbox.insert(tk.END, ciudad)
listbox.pack()
listbox.bind('<<ListboxSelect>>', seleccionar)

label = tk.Label(root, text='')
label.pack()

root.mainloop()