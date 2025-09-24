opcion = int(input("Inserta tu nota"))
match opcion:
    case 1|2|0:
        print("Muy deficiente")
    case 3|4:
        print("Suspenso")
    case 5:
        print("Aprobado")
    case 6:
        print("Bien")
    case 7|8:
        print("Notable")
    case 9:
        print("Sobresaliente")
    case 10:
        print("Matricula de honor")