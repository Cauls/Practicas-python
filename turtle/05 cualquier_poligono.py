import turtle as t

anguloLado = 180
lados = 0

while lados < 3:    
    lados = int(input('Inserta el numero de lados que tiene que tener el polígono: '))
anguloLado += (180*(lados-3))
anguloLado = anguloLado/lados
anguloLado = anguloLado/(0.5*(lados-2))
t.pensize(5)
t.pencolor('blue')
for i in range(lados):
    t.left(anguloLado)
    t.forward(100)