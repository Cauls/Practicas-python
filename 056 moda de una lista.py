lista = [1, 1, 3, 1, 5, 6, 6, 1, 2, 3, 4]
moda = [0, 0]
contador = 0
lista.sort()
for i in lista:
    if i == moda[0]:
        contador += 1

print(moda)
