import turtle as t

cursor = t.Turtle()
pantalla = t.Screen()

cursor.hideturtle()
cursor.speed(20)


def iniciar_dibujo(color):
    cursor.color(color)
    cursor.pendown()
    cursor.begin_fill()


def terminar_dibujo():
    cursor.end_fill()
    cursor.penup()


cursor.penup()

# ===================== #
# AQUÍ INICIA EL DIBUJO #
# ===================== #

cursor.goto(-150, 100)

# Cuadrado principal:
iniciar_dibujo("tan")
for _ in range(2):
    cursor.forward(300)
    cursor.right(90)
    cursor.forward(200)
    cursor.right(90)
terminar_dibujo()


# Ventana izquierda:
cursor.goto(-120, 30)
iniciar_dibujo("SlateGray1")
for _ in range(4):
    cursor.forward(50)
    cursor.right(90)
terminar_dibujo()
# Ventana derecha:
cursor.goto(70, 30)
iniciar_dibujo("SlateGray1")
for _ in range(4):
    cursor.forward(50)
    cursor.right(90)
terminar_dibujo()
# Puerta:
cursor.goto(-30, 20)
iniciar_dibujo("chocolate4")
for _ in range(2):
    cursor.forward(60)
    cursor.right(90)
    cursor.forward(120)
    cursor.right(90)
terminar_dibujo()
# Chimenea:
cursor.setheading(0)
cursor.goto(-100, 120)
iniciar_dibujo("LightSalmon4")
for _ in range(2):
    cursor.forward(40)
    cursor.left(90)
    cursor.forward(80)
    cursor.left(90)
terminar_dibujo()
# Tejado:
cursor.goto(-150, 100)
iniciar_dibujo("snow4")
cursor.forward(300)
cursor.right(210)
cursor.forward(171)
cursor.right(300)
cursor.forward(150)
terminar_dibujo()

pantalla.mainloop()
