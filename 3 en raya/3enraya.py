ganador = ""
turno = "X"
marco = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def imprimir(marco):
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
def comprobar(marco):
    global ganador
    if not any(" " in fila for fila in marco):
        ganador = "empate"
        print("Empate")
    for fila in marco:
        if fila[0] == fila[1] == fila[2]:
            ganador = fila[0]
        elif 

imprimir(marco)
while ganador == "":
    tirar(turno, marco)
    imprimir(marco)
    if turno == "X":
        turno = "O"
    elif turno == "O":
        turno = "X"
    comprobar(marco)