palabras = ["hola", "huevos", "buenas", "codigo"]
resultado = {}
for i in palabras:
    if i[0] not in resultado.keys():
        resultado.update({i[0]:1})
    else:
        resultado[i[0]] += 1
print(resultado)