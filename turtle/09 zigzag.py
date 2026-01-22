import turtle as t
import random as r

t.pensize(5)
t.pencolor('blue')
for i in range(10):
    numero = r.randint(0,360)
    t.rt(numero)
    numero = r.randint(0,360)
    t.fd(numero)
    numero = r.randint(0,360)
    t.lt(numero)
    numero = r.randint(0,360)
    t.fd(numero)
    
    