letras = ["a", "i", "e", "w", "f", "p", "r"]
contador = 0
for i in letras:
    for j in "aeiou":
        if i == j:
            contador+=1
print(contador)