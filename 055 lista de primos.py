numero = int(input("Inserta un numero"))
primos = []
for i in range(numero):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        print(" ", end="")
    else:
        primos.append(i)
print("")
print(primos)