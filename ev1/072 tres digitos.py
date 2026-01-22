numero = 1000
divisores = [2, 3, 5, 7, 11, 17, 19]
factores = []
while numero > 999 or numero < 0:
    numero = int(input("Inserta un numero de entre 1 a 3 digitos"))
    original = numero
while numero > 1:
    for i in divisores:
        if numero % i == 0:
            numero = numero/i
            factores.append(i)
            break
print(f"{original} = ", end="")
for i in factores:
    if i != factores[len(factores)-1]:
        print(f"{i}x", end="")
    else:
        print(i)