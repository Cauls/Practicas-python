producto = ""
precio = 0
productos = {}
valido = True
while valido == True:
    producto = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    if producto == "fin" or precio == "fin":
        valido = False
    else:
        precio = int(precio)
        productos.update({producto:precio})
print(productos)