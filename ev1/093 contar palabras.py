diccionario = {}
mayores = []
cosa = []
ordenado = False
frase = input("Inserta una frase: ").split(" ")
insertados = 0
for i in frase:
    if i in diccionario:
        diccionario[i][0] += 1
    else:
        diccionario[i] = [1, len(i)]
for i in diccionario:
    mayores.append([i, diccionario[i][0]])
while ordenado == False:
    ordenado = True
    for i in range(len(mayores)):
        if i != len(mayores)-1:
            if mayores[i][1] > mayores[i+1][1]:
                cosa = mayores[i + 1]
                mayores[i+1] = mayores[i]
                mayores[i] = cosa
                ordenado = False
while len(mayores) > 5:
    mayores.pop(0)
print(mayores)
print(diccionario)