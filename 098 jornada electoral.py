diccionario = {
    "carlos" : 0,
    "sergio" : 0,
    "misael" : 0,
    "gabriel" : 0
}
entrada = ""
while entrada != "fin":
    entrada = input("Inserta el candidato a votar: ")
    if entrada.lower() in diccionario:
        diccionario[entrada.lower()] += 1
mayor = ["",0]
for i in diccionario:
    if diccionario[i] > mayor[1]:
        mayor = [i, diccionario[i]]
print(diccionario, mayor)