numero1 = int(input("Introduce el primer numero"))
numero2 = int(input("Introduce el segundo numero"))
operador = input("Introduce la operación que quieras realizar (+, -, *, /)")
match operador:
    case "+":
        print(numero1 + numero2)
    case "-":
        print(numero1 - numero2)
    case "*":
        print(numero1 * numero2)
    case "/":
        print(numero1 / numero2)