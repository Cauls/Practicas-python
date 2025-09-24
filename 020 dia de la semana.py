opcion = input("Elige dia de la semana").lower()
match opcion:
    case "sabado"|"domingo":
        print("Dia festivo")
    case "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
        print("Dia laborable")
    case _:
        print("Escribe bien anda")