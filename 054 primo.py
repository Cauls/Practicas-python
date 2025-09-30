numero = int(input("Introduce un numero"))
if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
    print(f"El numero {numero} no es primo")
else:
    print(f"El numero {numero} es primo")