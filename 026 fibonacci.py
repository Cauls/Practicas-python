num1 = 0
num2 = 1
resultado = 0
ciclos = int(input("Inserta la cantidad de ciclos a realizar"))
for i in range(ciclos):
    resultado = num1 + num2
    print(f"{i + 1}. {num1} + {num2} = {resultado}")
    num1 = num2
    num2 = resultado