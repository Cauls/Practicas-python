ancho = int(input("Inserta el ancho"))
alto = int(input("Inserta el alto"))


for j in range(alto+1):
    if j == 0 or j == alto:
        print("*"*ancho)
    else:
        print("*" + " "*(ancho-2) + "*")
