lista = {
    "pescado" : 20,
    "carne" : 40,
    "queso" : 5
}
print(lista)
elemento = input("Inserta el elemento cuyo stock modificar: ")
operacion = input("Que quieres hacer con el valor? (-/+): ")
cambiar = int(input("Inserta el valor que modificarlo: "))
match(operacion):
    case "-":
        if cambiar > lista[elemento]:
            print("No se puede hacer la operacion")
        else:
            lista[elemento] = lista[elemento] - cambiar
    case "+":
        lista[elemento] = lista[elemento] + cambiar
print(lista)