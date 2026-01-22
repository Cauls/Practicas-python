lista = [1, 1, 3, 1, 5, 6, 6, 1, 2, 3, 4, 1]
moda = [0, 0]
previo = 0
candidato = [0, 0]
lista.sort()
for i in lista:
    actual = i
    if candidato[0] == i:
        candidato[1] += 1
    else:
        candidato = [i, 1]
    if candidato[1] > moda[1]:
        moda = candidato
print(moda)