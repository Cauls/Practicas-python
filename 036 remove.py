lista = ["rojo", "verde", "azul", "amarillo"]
for index, color in enumerate(lista):
    if color == "verde":
        lista.remove(lista[index])
print(lista)