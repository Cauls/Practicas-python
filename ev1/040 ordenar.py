numeros=[5, 2, 9, 1, 5, 6]
meneo = 0
ordenado = False
eleccion = int(input("Elige si quieres que sea 1. ascendente o 2. descendente"))
match eleccion:
    case 1:
        while ordenado == False:
            ordenado = True
            for i in range(int(len(numeros)-1)):
                if numeros[i] > numeros[i+1]:
                    meneo = numeros[i]
                    numeros[i] = numeros[i+1]
                    numeros[i+1] = meneo
                    ordenado = False
    case 2:
        while ordenado == False:
            ordenado = True
            for i in range(int(len(numeros)-1)):
                if numeros[i] < numeros[i+1]:
                    meneo = numeros[i]
                    numeros[i] = numeros[i+1]
                    numeros[i+1] = meneo
                    ordenado = False
print(numeros)