import random
rangoinf = int(input("Inserta el rango minimo"))
rangosup = int(input("Inserta el rango maximo"))
cantidad = int(input("Inserta la cantidad de numeros"))
for i in range(cantidad):
    print(random.randint(rangoinf, rangosup))