nombres=["figue","wassim","hugo","sergio","alex"]
meneo = 0
ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(int(len(nombres)-1)):
        if nombres[i] > nombres[i+1]:
            meneo = nombres[i]
            nombres[i] = nombres[i+1]
            nombres[i+1] = meneo
            ordenado = False
print(nombres)