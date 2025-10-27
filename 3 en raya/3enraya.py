#Se importa random para los turnos en los que tire la maquina, en estos turnos el valor se decidirá de forma aleatoria y se comprobará que la posición elegida sea válida
import random

#Aqui se hayan las únicas variables necesarias para el programa
#Ganador: Almacena el jugador que ha ganado (X o O). La mayor parte del tiempo se mantendrá con un string vacio para mantener el bucle ciclando. Sirve como herramienta de control de bucle, cerrándolo una vez se haya ganado.
ganador = ""
#Turno: Esta variable es la única responsable de decidir que simbolo juega en cada turno, altenando entre X y O dependiendo de que símbolo haya tirado en el anterior turno
turno = "X"
#Marco: Este array almacena el valor de cada casilla. Los espacios son los valores por defecto y se van cambiando por símbolos a medida que se vayan seleccionando por los jugadores
marco = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#X e Y: Estas variables sirven para elegir en que posición se quiere poner el símbolo como veremos mas adelante
X = 0
Y = 0
#Eleccion: Se encarga de elegir que modo de juego se va a jugar, se lo pide al jugador mediante un input
eleccion = int(input("Elige el modo de juego\n1)Jugador contra jugador\n2)Jugador contra máquina\n3)Maquina contra maquina"))

#Funcion encargada de imprimir las casillas, al ser llamada imprimirá cada valor de forma ordenada, se podría modificar para imprimir tableros de mas de 3x3
def imprimir():
    global marco
    print("  0   1   2  ")
    for indice, valor in enumerate(marco):
        print(f"{indice} {valor[0]} | {valor[1]} | {valor[2]} | ")

#Funcion encargada de la tirada del jugador, se le inserta la variable turno como parametro jugador para saber que símbolo tiene que insertar y marco para saber en que estado esta el mapa y que casillas estan ocupadas
def tirar(jugador, marco):
    print(f"Turno del jugador {jugador}:")
    #Valida se encarga de controlar que la posición insertada no esté ocupada mediante el siguiente bucle while
    valida = False
    #Valida siempre ser False a no ser que la posición insertada tenga un espacio como caracter
    while valida == False:
        x = int(input("Inserta en eje x (0-2)"))
        y = int(input("Inserta en eje y (0-2)"))
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
def comprobar():
    global marco
    global ganador
    #Comprueba cada fila horizontal, si alguna está ocupada por un sólo símbolo asignará ese símbolo como ganador
    for fila in marco:
        if fila[0] != " " and fila[0] == fila[1] and  fila[0] == fila[2]:
            ganador = fila[0]
            print(f"Ha ganado el jugador {ganador}")
            break
    #Comprueba cada fila vertical, de nuevo, si alguna esta ocupada por un solo jugador este ganará
    for indice in range(0, 3):
        if marco[0][indice] !=" " and marco[0][indice] == marco[1][indice] and marco[0][indice] == marco[2][indice]:
            ganador = marco[0][indice]
            print(f"Ha ganado el jugador {ganador}")
            break
    #Comprueba la diagonal, para ello, comprueba las esquinas adyacentes y si son iguales a la casilla central, ese jugador ganará
    if marco[1][1] != " " and (marco[1][1] == marco[0][0] == marco[2][2] or marco[1][1] == marco[0][2] == marco[2][0]):
        ganador = marco[1][1]
        print(f"Ha ganado el jugador {ganador}")
    #Este condicional comprueba que haya casillas no elegidas aun, en caso de que no se cumplan el resto
    if not any(" " in fila for fila in marco):
        ganador = "empate"
        print("Empate")

#Switch dedicado a decidir que modo de juego se jugará, si jugador contra jugador, jugador contra maquina o maquina contra maquina
match eleccion:
    case 1:
        #El modo jugador contra jugador, primero imprime el tablero
        imprimir()
        #Mientras no haya ganador, tira con el jugador que haya seleccionado, imprime el tablero y cambia el jugador al que le toca ahora
        while ganador == "":
            tirar(turno, marco)
            imprimir()
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            #Por ultimo, comprueba si se ha ganado o empatado ya
            comprobar()
    case 2:
        #El modo jugador contra maquina, es muy parecido al anterior modo
        imprimir()
        while ganador == "":
            #Aqui la mayor diferencia, es que comprueba que jugador es antes de decidir si va a tirar la maquina o el jugador, forzando siempre al jugador a ser la X
            if turno == "X":
                tirar(turno, marco)
                imprimir()
                turno = "O"
            elif turno == "O":
                tiradaBot(turno, marco)
                imprimir()
                turno = "X"
            comprobar()
    case 3:
        imprimir()
        while ganador == "":
            #Exactamente igual que con el jugador contra jugador pero haciendo que tire la maquina
            tiradaBot(turno, marco)
            imprimir()
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            comprobar()