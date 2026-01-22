diccionario = {
    "España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"],
    "Francia": ["París", "Marsella", "Lyon", "Toulouse", "Niza"],
    "Italia": ["Roma", "Milán", "Nápoles", "Turín", "Florencia"],
    "Alemania": ["Berlín", "Múnich", "Hamburgo", "Colonia", "Fráncfort"],
    "Estados Unidos": ["Nueva York", "Los Angeles", "Chicago", "Houston", "Miami"]
}
encontrado = False
busca = input("Inserta el elemento a buscar: ")
if busca in diccionario:
    print(diccionario[busca])
    encontrado = True
else:
    for i in diccionario:
        if busca in diccionario[i]:
            print("La ciudad " + busca + " se halla en " + i)
            encontrado = True
if encontrado == False:
    print("El elemento " + busca + " no está o está mal escrito")
