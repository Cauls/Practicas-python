import turtle as t
import tkinter as tk

ventana = t.Screen()
ventana.bgcolor('lightblue')

x = t.Turtle()

x.shape('turtle')
x.color('red')
x.pensize(3)
x.pencolor('green')

for i in range(4):
    x.forward(100)
    x.right(90)

t.done()