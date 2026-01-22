productos = {
    "pan" : 1.5,
    "leche" : 0.9,
    "huevos" : 2.5,
    "carne" : 5.0,
    "pescado" : 4.0
}
descuento = int(input("Inserta el descuento a recibir: "))
for i in productos:
    print(f"{i} : {round(productos[i] - (productos[i] / 100 * descuento),2)}")
