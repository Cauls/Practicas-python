#Se importa random para los turnos en los que tire la maquina, en estos turnos el valor se decidirá de forma aleatoria y se comprobará que la posición elegida sea válida
import random

#Funcion encargada de imprimir las casillas, al ser llamada imprimirá cada valor de forma ordenada, se podría modificar para imprimir tableros de mas de 3x3
def imprimir(marco):
    print("  0   1   2  ")
    for indice, valor in enumerate(marco):
        print(f"{indice} {valor[0]} | {valor[1]} | {valor[2]} | ")

#Funcion encargada de la tirada del jugador, se le inserta la variable turno como parametro jugador para saber que símbolo tiene que insertar y marco para saber en que estado esta el mapa y que casillas estan ocupadas
def tirar(jugador, marco):
    print(f"Turno del jugador {jugador}:")
    #Valida se encarga de controlar que la posición insertada no esté ocupada mediante el siguiente bucle while
    valida = False
    #Valida siempre ser False a no ser que la posición insertada tenga un espacio como caracter y las coordenadas esten dentro del marco
    while valida == False:
        x = int(input("Inserta en eje x (0-2)"))
        y = int(input("Inserta en eje y (0-2)"))
        if x >= 0 and y >= 0 and x < 3 and y < 3:
            if marco[x][y] == " ":
                marco[x][y] = jugador
                valida = True
        else:
            print("Inserta un valor válido")

#Funcion muy similar a tirar, pero usada para la maquina, usa el random para hacer tiradas hasta que caiga una válida
def tiradaBot(jugador, marco):
    print(f"Turno del jugador {jugador}:")
    valida = False
    while valida == False:
        #Esta es la mayor diferencia, en vez de pedir la posicion, la genera de forma aleatoria
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if marco[x][y] == " ":
            marco[x][y] = jugador
            valida = True

#Funcion que se ejecutará tras cada tirada, se encarga de comrpobar que no haya diagonales ni líneas, en caso de que las haya asigna un ganador y termina el bucle
def comprobar(marco, ganador):
    #Comprueba cada fila horizontal, si alguna está ocupada por un sólo símbolo asignará ese símbolo como ganador
    for fila in marco:
        if fila[0] != " " and fila[0] == fila[1] and  fila[0] == fila[2]:
            ganador = fila[0]
            print(f"Ha ganado el jugador {ganador}")
            return ganador
    #Comprueba cada fila vertical, de nuevo, si alguna esta ocupada por un solo jugador este ganará
    for indice in range(0, 3):
        if marco[0][indice] !=" " and marco[0][indice] == marco[1][indice] and marco[0][indice] == marco[2][indice]:
            ganador = marco[0][indice]
            print(f"Ha ganado el jugador {ganador}")
            return ganador
    #Comprueba la diagonal, para ello, comprueba las esquinas adyacentes y si son iguales a la casilla central, ese jugador ganará
    if marco[1][1] != " " and (marco[1][1] == marco[0][0] == marco[2][2] or marco[1][1] == marco[0][2] == marco[2][0]):
        ganador = marco[1][1]
        print(f"Ha ganado el jugador {ganador}")
        return ganador
    elif not any(" " in fila for fila in marco) and ganador == "":
        #Este condicional comprueba que haya casillas no elegidas aun, en caso de que no se cumplan el resto
        ganador = "empate"
        print("Empate")
        return ganador
    else:
        return ""
