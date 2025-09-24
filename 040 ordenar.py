numeros=[5, 2, 9, 1, 5, 6]
meneo = 0
ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(int(len(numeros)-1)):
        if numeros[i] > numeros[i+1]:
            meneo = numeros[i]
            numeros[i] = numeros[i+1]
            numeros[i+1] = meneo
            ordenado = False
print(numeros)