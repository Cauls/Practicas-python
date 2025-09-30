lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista = []
for i in range(len(lista1)):
    lista.append(lista1[i])
    lista.append(lista2[i])
print(lista)