lista =[-1, -2, -3, 4, 5, -6, -7]
contador = 0
for i in lista:
    if i < 0:
        print(i)
        contador += 1
print(f"Hay {contador} numeros negativos")
