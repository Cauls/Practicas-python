ancho = int(input("Inserta el ancho"))
alto = int(input("Inserta el alto"))

for i in range(alto):
    if i == alto/2 or i == alto//2:
        print("*"*ancho)
    else:
        print("*" + " "*(ancho-2) + "*")