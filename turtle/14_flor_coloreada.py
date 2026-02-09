import turtle as t

cursor = t.Turtle()
pantalla = t.Screen()

cursor.speed(100)
cursor.color("red")
cursor.begin_fill()

for _ in range(8):
    cursor.color("red")
    cursor.begin_fill()
    cursor.circle(90)
    cursor.end_fill()
    cursor.left(45)


cursor.penup()
cursor.goto(0, -50)
cursor.pendown()

cursor.color("yellow")
cursor.begin_fill()
cursor.circle(50)
cursor.end_fill()

pantalla.mainloop()
