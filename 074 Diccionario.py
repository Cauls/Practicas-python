diccionario = {
    "apple":"manzana",
    "orange":"naranja",
    "banana":"platano",
    "pear":"pera",
    "watermelon":"sandia"
}
frase = input("Inserta una fruta ")
if frase in diccionario:
    print(diccionario[frase])
else:
    print("Fruta no encontrada")