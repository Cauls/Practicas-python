lista = [("Pepe", 200), ("Juanito", 150), ("Pitingo", 50), ("Optimus_Prime", 300), ("Pitingo", 50), ("Optimus_Prime", 300), ("Juanito", 150)]
diccionario = {}
for i in lista:
    if i[0] in diccionario:
        diccionario[i[0]] += i[1]
    else:
        diccionario.update({i[0]:i[1]})
print(diccionario)
ranking_ordenado = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
print(ranking_ordenado)