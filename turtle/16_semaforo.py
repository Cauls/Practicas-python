import turtle as t

cursor = t.Turtle()
pantalla = t.Screen()

cursor.speed(20)
cursor.hideturtle()


def imprimir_circulo():
    cursor.pendown()
    cursor.begin_fill()
    cursor.circle(50)
    cursor.end_fill()
    cursor.penup()


cursor.up()

cursor.goto(-60, 220)
cursor.color("gray")
cursor.pendown()
cursor.begin_fill()
for _ in range(2):
    cursor.forward(120)
    cursor.right(90)
    cursor.forward(340)
    cursor.right(90)
cursor.end_fill()
cursor.penup()

cursor.goto(0, 110)
cursor.color("red")
imprimir_circulo()

cursor.goto(0, 0)
cursor.color("yellow")
imprimir_circulo()

cursor.goto(0, -110)
cursor.color("green")
imprimir_circulo()

pantalla.mainloop()
