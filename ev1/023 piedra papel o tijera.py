num1 = int(input("Elige: 1.Piedra 2.Papel 3.Tijeras"))
num2 = int(input("Elige: 1.Piedra 2.Papel 3.Tijeras"))
match num1:
    case 1:
        if num2==1:
            print("Empate")
        elif num2==2:
            print("Has perdido")
        elif num2==3:
            print("Has ganado")
    case 2:
        if num2==1:
            print("Has ganado")
        elif num2==2:
            print("Empate")
        elif num2==3:
            print("Has perdido")
    case 3:
        if num2==1:
            print("Has perdido")
        elif num2==2:
            print("Has ganado")
        elif num2==3:
            print("Empate")
    case _:
        print("Elige bien")