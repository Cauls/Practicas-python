peso = float(input("Inserta tu peso, gordito"))
altura = float(input("Inserta tu altura en centimetros")) / float(100)
imc = float(peso) / float(altura**2)
print(imc)