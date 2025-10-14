numero = 1000
centenas = 0
decenas = 0
unidades = 0
while numero > 999 or numero < 0:
    numero = int(input("Inserta un numero de entre 1 a 3 digitos"))
while numero >= 100:
    centenas += 1
    numero -= 100
while numero >= 10:
    decenas += 1
    numero -= 10
while numero > 0:
    unidades += 1
    numero -= 1
print(f"{centenas} centenas, {decenas} decenas y {unidades} unidades")