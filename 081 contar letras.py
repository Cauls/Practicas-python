diccionario = {}
frase = input("Inserta una frase")
for i in frase:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(diccionario)

diccionario = {}
frase = input("Inserta una frase").split(" ")
for i in frase:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(diccionario)