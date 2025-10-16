import random

ganador = ""
turno = "X"
marco = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
X = 0
Y = 0
eleccion = int(input("Elige el modo de juego\n1)Jugador contra jugador\n2)Jugador contra máquina\n3)Maquina contra maquina"))
def imprimir():
    global marco
    print("  0   1   2  ")
    for indice, valor in enumerate(marco):
        print(f"{indice} {valor[0]} | {valor[1]} | {valor[2]} | ")
def tirar(jugador, marco):
    print(f"Turno del jugador {jugador}:")
    valida = False
    while valida == False:
        x = int(input("Inserta en eje x (0-2)"))
        y = int(input("Inserta en eje y (0-2)"))
        if marco[x][y] == " ":
            marco[x][y] = jugador
            valida = True
        else:
            print("Inserta un valor válido")
def tiradaBot(jugador, marco):
    print(f"Turno del jugador {jugador}:")
    valida = False
    while valida == False:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if marco[x][y] == " ":
            marco[x][y] = jugador
            valida = True
def comprobar():
    global marco
    global ganador
    for fila in marco:
        if fila[0] != " " and fila[0] == fila[1] and  fila[0] == fila[2]:
            ganador = fila[0]
            print(f"Ha ganado el jugador {ganador}")
            break
    for indice in range(0, 3):
        if marco[0][indice] !=" " and marco[0][indice] == marco[1][indice] and marco[0][indice] == marco[2][indice]:
            ganador = marco[0][indice]
            print(f"Ha ganado el jugador {ganador}")
            break
    if marco[1][1] != " " and (marco[1][1] == marco[0][0] == marco[2][2] or marco[1][1] == marco[0][2] == marco[2][0]):
        ganador = marco[1][1]
        print(f"Ha ganado el jugador {ganador}")
    if not any(" " in fila for fila in marco):
        ganador = "empate"
        print("Empate")

match eleccion:
    case 1:
        imprimir()
        while ganador == "":
            tirar(turno, marco)
            imprimir()
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            comprobar()
    case 2:
        imprimir()
        while ganador == "":
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
            tiradaBot(turno, marco)
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            comprobar()