opcion = int(input("Elige opcion: 1=Saludar, 2=Despedirse, 3=Salir"))
match opcion:
    case 1:
        print("Hola")
    case 2:
        print("Adios")
    case 3:
        print("Me voy")
    case _:
        print("Opcion no reconocida")