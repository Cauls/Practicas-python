numeros = [3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96, 15, 41, 68, 99]
mayores = []
numero = int(input("Inserta un numero"))
meneo = 0
ordenado = False
for i in numeros:
    if i > numero and i not in mayores:
        mayores.append(i)
while ordenado == False:
            ordenado = True
            for i in range(int(len(mayores)-1)):
                if mayores[i] > mayores[i+1]:
                    meneo = mayores[i]
                    mayores[i] = mayores[i+1]
                    mayores[i+1] = meneo
                    ordenado = False
print(mayores)