import turtle as t

pantalla = t.Screen()
cursor = t.Turtle()
cursor.hideturtle()

# Cuadrado azul:
cursor.color("blue")
cursor.begin_fill()
for _ in range(4):
    cursor.forward(100)
    cursor.right(90)
cursor.end_fill()

# Muevo el bolígrafo:
cursor.penup()
cursor.goto(150, 0)
cursor.pendown()

# Cuadrado rojo:
cursor.color("red")
cursor.begin_fill()
for _ in range(4):
    cursor.forward(100)
    cursor.right(90)
cursor.end_fill()

pantalla.mainloop()
