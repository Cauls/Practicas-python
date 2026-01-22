alumnos = {
    "Wassim": {"nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
    "Juan": {"nota1": 5.0, "nota2": 6.0, "nota3": 7.0},
    "Emily": {"nota1": 9.0, "nota2": 8.5, "nota3": 9.5},
    "Raúl": {"nota1": 4.0, "nota2": 3.5, "nota3": 3.0}
}
iter = 0
lista = []
for i in alumnos:
    media = 0
    for j in alumnos[i]:
        media += alumnos[i][j]
    lista.append([i, media])
maximo = ["", 0]
minima = ["", 100]
for i in lista:
    if i[1] > maximo[1]:
        maximo = i
    if i[1] < minima[1]:
        minima = i
print(f"El/la alumno/a con la mayor media es {maximo[0]} con una media de {maximo[1]}")
print(f"El/la alumno/a con la menor media es {minima[0]} con una media de {minima[1]}")