tipo = int(input("Quieres sacar el area o el perímetro? 1.Area 2.Perimetro"))
forma = input("De que forma?").lower()
match forma:
    case "cuadrado":
        match tipo:
            case 1:
                lado = int(input("Inserta la longitud del lado"))
                print(lado*lado)
            case 2:
                lado = int(input("Inserta la longitud del lado"))
                print(lado*4)
    case "rectangulo":
        match tipo:
            case 1:
                lado = int(input("Inserta el ancho"))
                lado1 = int(input("Inserta el largo"))
                print(lado1*lado)
            case 2:
                lado = int(input("Inserta el ancho"))
                lado1 = int(input("Inserta el largo"))
                print(lado*2+lado1*2)
    case "triangulo":
        match tipo:
            case 1:
                lado = int(input("Inserta la base"))
                lado1 = int(input("Inserta la altura"))
                print(lado*lado1/2)
            case 2:
                lado = int(input("Inserta el primer lado"))
                lado2 = int(input("Inserta el segundo lado"))
                lado3 = int(input("Inserta el tercer lado"))
                print(lado + lado2 + lado3)
    case "rombo":
        match tipo:
            case 1:
                diagonal = int(input("Inserta la diagonal corta"))
                diagonal2 = int(input("Inserta la diagonal larga"))
                print(diagonal * diagonal2 / 2)
            case 2:
                lado = int(input("Inserta el lado"))
                print(lado * 4)
    case "pentagono":
        match tipo:
            case 1:
                lado = int(input("Inserta un lado"))
                apotema = int(input("Inserta el apotema"))
                print(5*lado*apotema/2)
            case 2:
                lado = int(input("Inserta el lado"))
                print(lado*5)
    case "hexagono":
        match tipo:
            case 1:
                lado = int(input("Inserta el lado"))
                apotema = int(input("Inserta el apotema"))
                print(6*lado*apotema/2)
            case 2:
                lado = int(input("Inserta el lado"))
                print(6*lado)