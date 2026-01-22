diccionario = {
    "Python":[8,9,10],
    "Sostenibilidad":[5, 7, 5],
    "Digitalizacion":[8, 8, 7]
}
for i in diccionario:
    print(f"{i} : {sum(diccionario[i])//3}")