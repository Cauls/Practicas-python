import turtle as t

def cuadrado(t):
    for i in range(4):
        t.fd(200)
        t.lt(90)

def triangulo(t):
    t.lt(60)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    t.lt(90)

t.pensize(5)
t.pencolor('blue')
triangulo(t)
t.penup
t.goto(0,0)
cuadrado(t)