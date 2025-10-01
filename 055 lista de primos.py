numero = int(input("Inserta un numero"))
primos = []
for i in range(numero):
    if i == 2 or i == 3 or i == 5 or i == 7:
        primos.append(i)
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(" ", end="")
    else:
        primos.append(i)
print("")
print(primos)