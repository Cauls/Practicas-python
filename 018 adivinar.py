import random
valor = random.randrange(0,100)
intentos = 4
intento = 0
while valor!=intento & intentos > 0:
    intento = int(input("Inserta un numero"))
    if valor > intento:
        print("El numero es mayor")
        intentos -= 1
    elif valor < intento:
        print("El numero es menor")
        intentos -= 1
    elif valor == intento:
        print("Lo has adivinado")