import random as r
ganador = 'none'
barcosj1 = {}
barcosj2 = {}

def printTablero(tablero):
    print(' ' + '-'*((len(tablero)*3)-1))
    for i in range(len(tablero)):
        print(f'{i}|', end='')
        for j in range(len(tablero)):
            print(f' {tablero[i][j]} ', end='')
        print('|')
    print(' ' + '-'*((len(tablero)*3)-1))

def genBarcos(tableroj1, tableroj2):
    global barcos
    barcos = [3, 3, 4, 2]
    coord = [0,0]
    indice = 1
    angulo = ''
    for i in barcos:
        while colocarValido(tableroj1, coord[0], coord[1], i, angulo) == False:
            coord = randomCoord(tableroj1)
            angulo = randomAngulo()
        match angulo:
            case 'H':
                for j in range(coord[1], coord[1]+i):
                    tableroj1[coord[0]][j] = f'{indice}'
            case 'V':
                for j in range(coord[0], coord[0]+i):
                    tableroj1[j][coord[1]] = f'{indice}'
        barcosj1.update({indice : i})
    for i in barcos:
        while colocarValido(tableroj2, coord[0], coord[1], i, angulo) == False:
            coord = randomCoord(tableroj2)
            angulo = randomAngulo()
        match angulo:
            case 'H':
                for j in range(coord[1], coord[1]+i):
                    tableroj2[coord[0]][j] = f'{indice}'
            case 'V':
                for j in range(coord[0], coord[0]+i):
                    tableroj2[j][coord[1]] = f'{indice}'
        barcosj2.update({indice : i})


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

def comprobarBarcos(tableroj1, tablerofalsoj1, tableroj2, tablerofalsoj2):
    global barcosj1, barcosj2
    for i in barcosj1:
        if barcosj1[i] == 0:
            hundirBarcos(i, tableroj1, tablerofalsoj1)
            print(f'Jugador 2 ha derribado el barco {i}')
    for i in barcosj2:
        if barcosj2[i] == 0:
            hundirBarcos(i, tableroj2, tablerofalsoj2)
            print(f'Jugador 1 ha derribado el barco {i}')
    

def hundirBarcos(eliminar, tablero, tablerofalso):
    for i in range(len(tablero)-1):
        for j in range(len(tablero)-1):
            if tablero[i][j] == eliminar:
                tablerofalso[i][j] == '🕳️'
            
        
def ataquej1(tablero, tableroReal):
    fila = 15
    col = 15
    print('Turno del Jugador 1')
    while verificarAtaque(fila, col, tablero) == False:
        fila = int(input('Jugador 1, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case default:
            tablero[fila][col] = '💥'
            barcosj1[tableroReal[fila][col]] -= 1

def ataquej2(tablero, tableroReal):
    fila = 15
    col = 15
    print('Turno del Jugador 2')
    while verificarAtaque(fila, col, tablero) == False:
        fila = int(input('Jugador 2, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case default:
            tablero[fila][col] = '💥'
            barcosj1[tableroReal[fila][col]] -= 1

def ataquebotj1(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) == False:
        fila = r.randint(0, len(tablero)-1)
        col = r.randint(0, len(tablero)-1)
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case default:
            tablero[fila][col] = '💥'
            barcosj2[tableroReal[fila][col]] -= 1

def ataquebotj2(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) == False:
        fila = r.randint(0, len(tablero)-1)
        col = r.randint(0, len(tablero)-1)
    match tableroReal[fila][col]:
        case '.':
            tablero[fila][col] = '💧'
        case default:
            tablero[fila][col] = '💥'
            barcosj1[tableroReal[fila][col]] -= 1
    

def checkVictoria():
    global barcosj1, barcosj2
    ganador = 'J2'
    for i in barcosj1:
        if barcosj1[i] != 0:
            ganador = 'none'
    ganador = 'J1'
    for i in barcosj2:
        if barcosj2[i] != 0:
            ganador = 'none'
    return ganador