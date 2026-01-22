import tkinter as tk
print("Tkinter versión:", tk.TkVersion)
root = tk.Tk()
root.title("Test")
tk.Label(root, text="Funciona!").pack()
root.mainloop()