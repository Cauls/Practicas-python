numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
ordenado = False
meneo = 0
while ordenado == False:
    ordenado = True
    for i in range(int(len(numeros)-1)):
        if numeros[i] > numeros[i +1]:
            meneo=numeros[i]
            numeros[i]=numeros[i+1]
            numeros[i+1]=meneo
            ordenado=False
print(numeros[-3], numeros[-2], numeros[-1])