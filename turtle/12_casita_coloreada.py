import turtle as t

pantalla = t.Screen()
cursor = t.Turtle()
cursor.hideturtle()

cursor.color("blue")
cursor.begin_fill()
for _ in range(4):
    cursor.forward(200)
    cursor.right(90)
cursor.end_fill()

cursor.color("yellow")
cursor.begin_fill()
for _ in range(3):
    cursor.forward(200)
    cursor.left(120)
cursor.end_fill()

pantalla.mainloop()
