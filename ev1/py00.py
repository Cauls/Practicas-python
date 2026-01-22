palabra = input("Inserta una palabra")
vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
numvocales = 0
for i in palabra:
    for j in vocales:
        if i == j:
            numvocales += 1
print(numvocales)