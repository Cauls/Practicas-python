import turtle as t

petalos = 5
giro = 360/petalos
t.pensize(5)
t.pencolor('blue')
for i in range(petalos):
    t.circle(50)
    t.left(giro)