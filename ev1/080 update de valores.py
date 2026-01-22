diccionario = {
    "Leche":[1, 20],
    "Huevos":[1.5, 15],
    "Atun":[3, 10]
}
print(diccionario)
valor = input("Pon el nombre del producto a cambiar")
precio = input("Escribe el nuevo precio")
diccionario.update({valor : [precio, diccionario[valor][1]]})
print(diccionario)