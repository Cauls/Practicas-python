import random as r
ataque = [0, 0]

def printTablero(tablero):
    print(' ' + '-'*((len(tablero)*3)-1))
    for i in range(len(tablero)-1):
        print(f'{i}|', end='')
        for j in range(len(tablero)-1):
            print(f' {tablero[i][j]} ', end='')
        print('|')
    print(' ' + '-'*((len(tablero)*3)-1))

def genBarcos(tablero):
    barcos = [3, 3, 4, 2]
    coord = [0,0]
    angulo = ''
    valida = False
    valida1 = False
    for i in barcos:
        while colocarValido(tablero, coord[0], coord[1], i, angulo) == False:
            coord = randomCoord(tablero)
            angulo = randomAngulo()
        match angulo:
            case 'H':
                for j in range(coord[1], coord[1]+i):
                    tablero[coord[0]][j] = 'X'
            case 'V':
                for j in range(coord[0], coord[0]+i):
                    tablero[j][coord[1]] = 'X'


def colocarValido(tablero, fila, col, barco, angulo):
    valido = True
    match angulo:
        case 'H':
            if col + barco > len(tablero)-1:
                valido = False
            else:
                for i in range(col, col+barco):
                    if tablero[fila][i] != '.':
                        valido = False
            
        case 'V':
            if fila + barco > len(tablero)-1:
                valido = False
            else:
                for i in range(fila, fila+barco):
                    if tablero[i][col] != '.':
                        valido = False
        case default:
            valido = False
    return valido

def randomCoord(tablero):
    coord = [0, 0]
    valido = False
    while valido == False:
        coord[0] = r.randint(0, len(tablero)-1)
        coord[1] = r.randint(0, len(tablero)-1)
        if coord[0] != coord[1]:
            valido = True
    return coord

def randomAngulo():
    valor = r.randint(0,1)
    match valor:
        case 0: 
            return 'H'
        case 1:
            return 'V'
        
def verificarAtaque(fila, col, tablero):
    if isinstance(fila, int) and isinstance(col, int):
        if fila < len(tablero) and col < len(tablero):
            if tablero[fila][col] == '.':
                return True
    return False
        
def ataquej1(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) == False:
        fila = int(input('Jugador 1, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case 'X':
            tablero[fila][col] = '💥'

def ataquej2(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) != False:
        fila = int(input('Jugador 2, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case 'X':
            tablero[fila][col] = '💥'

def ataquebot(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) != False:
        fila = r.randint(0, len(tablero)-1)
        col = r.randint(0, len(tablero)-1)
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case 'X':
            tablero[fila][col] = '💥'