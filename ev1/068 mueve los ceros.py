numeros = [0, 1, 0, 3, 12, 0, 5]
for i in numeros:
    if i == 0:
        numeros.append(i)
        numeros.remove(i)
print(numeros)