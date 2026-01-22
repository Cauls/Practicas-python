import turtle

t = turtle.Turtle()
pantalla = turtle.Screen()

def arriba():
    t.forward(20)

def izquierda():
    t.left(15)

def derecha():
    t.right(15)

pantalla.listen()
pantalla.onkey(arriba, "Up")
pantalla.onkey(izquierda, "Left")
pantalla.onkey(derecha, "Right")

turtle.mainloop()