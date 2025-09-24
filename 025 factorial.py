factorial = int(input("Introduce un numero para calcular su factorial")) + 1
resultado = 1
for i in range(1, factorial):
    resultado = resultado * i
print(resultado)