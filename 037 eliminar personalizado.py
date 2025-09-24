lista = ["rojo", "verde", "azul", "amarillo"]
eliminar = input("Elige el color para eliminar")
for index, color in enumerate(lista):
    if color == eliminar:
        lista.remove(lista[index])
print(lista)