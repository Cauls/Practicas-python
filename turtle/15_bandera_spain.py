import turtle as t

pantalla = t.Screen()
cursor = t.Turtle()
cursor.hideturtle()

cursor.speed(100)


def imprimir_rectangulo():
    for _ in range(2):
        cursor.forward(200)
        cursor.right(90)
        cursor.forward(40)
        cursor.right(90)


cursor.penup()
cursor.goto(-100, 20)  # 40 px de ancho 200 px de largo
cursor.pendown()

cursor.begin_fill()
cursor.color("red")
imprimir_rectangulo()
cursor.end_fill()

cursor.begin_fill()
cursor.penup()
cursor.goto(-100, -20)  # 40 px de ancho 200 px de largo
cursor.pendown()

cursor.begin_fill()
cursor.color("yellow")
imprimir_rectangulo()
cursor.end_fill()

cursor.penup()
cursor.goto(-100, -60)  # 40 px de ancho 200 px de largo
cursor.pendown()

cursor.begin_fill()
cursor.color("purple")
imprimir_rectangulo()
cursor.end_fill()

pantalla.mainloop()
