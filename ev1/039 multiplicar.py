numeros = [1, 2, 2, 3, 4, 4, 4, 5]
multi = int(input("Indica el numero por el que multiplicar"))
for index, valor in enumerate(numeros):
    numeros[index] = valor * multi
print(numeros)