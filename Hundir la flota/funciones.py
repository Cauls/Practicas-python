import random as r

#Dos diccionarios que almacenarán los barcos restantes de cada jugador junto a los segmentos que le quedan a cada barco
barcosj1 = {}
barcosj2 = {}

#Funció auxiliar, simplemente imprime el tablero de forma mas organizada
def printTablero(tablero):
    print(' ' + '-'*((len(tablero)*3)-1))
    for i in range(len(tablero)):
        print(f'{i}|', end='')
        for j in range(len(tablero)):
            print(f' {tablero[i][j]} ', end='')
        print('|')
    print(' ' + '-'*((len(tablero)*3)-1))

#Genera los barcos en los tableros ya creados pero vacíos, para ello usa unas cuantas funciones auxiliares que explicaré en breve, pero básicamente genera una posición aleatoria para cada barco y comprueba que sea válida, si lo es, generará el barco con su respectivo ID
def genBarcos(tableroj1, tableroj2):
    global barcos
    barcos = [3, 4]
    coord = [99,99]
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
        barcosj1.update({f'{indice}': i})
        indice += 1
    coord = [99,99]
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
        barcosj2.update({f'{indice}': i})
        indice += 1

#Funcion auxiliar que se encarga de determinar que una posición sea o no válida, comprobará que en su posición haya espacio suficiente para posicionar el barco, comprobando que no se salga de indice ni toque otro barco
def colocarValido(tablero, fila, col, barco, angulo):
    valido = True
    match angulo:
        case 'H':
            if col + barco > len(tablero)-1:
                valido = False
            else:
                for i in range(col, col+barco):
                    if tablero[fila][i] != '. ':
                        valido = False
            
        case 'V':
            if fila + barco > len(tablero)-1:
                valido = False
            else:
                for i in range(fila, fila+barco):
                    if tablero[i][col] != '. ':
                        valido = False
        case _:
            valido = False
    return valido

#Devuelve una posición aleatoria basándose en el tamaño del tablero dado
def randomCoord(tablero):
    coord = [0, 0]
    coord[0] = r.randint(0, len(tablero)-1)
    coord[1] = r.randint(0, len(tablero)-1)
    return coord

#Genera un angulo aleatorio, este puede ser horizontal o verical
def randomAngulo():
    valor = r.randint(0,1)
    match valor:
        case 0: 
            return 'H'
        case 1:
            return 'V'

#Esta función determinará si una coordenada dada es válida para ataque, para ello, debe ser dos números, ambos inferiores a la longitud del tablero y cuya posición no haya sido atacada previamente        
def verificarAtaque(fila, col, tablero):
    if isinstance(fila, int) and isinstance(col, int):
        if fila < len(tablero) and col < len(tablero):
            if tablero[fila][col] == '. ':
                return True
    return False

#Función auxiliar que comprobará cuantos segmentos le quedan a cada barco, en caso de que le queden 0, lo anunciará además de establecer sus segmentos en 9 para controlarlo más adelante
def comprobarBarcos(tableroj1, tablerofalsoj1, tableroj2, tablerofalsoj2):
    global barcosj1, barcosj2
    for i in barcosj1:
        if barcosj1[i] == 0:
            hundirBarcos(i, tableroj1, tablerofalsoj1)
            print(f'Jugador 2 ha derribado el barco {i}')
            barcosj1[i] = 9
    for i in barcosj2:
        if barcosj2[i] == 0:
            hundirBarcos(i, tableroj2, tablerofalsoj2)
            print(f'Jugador 1 ha derribado el barco {i}')
            barcosj2[i] = 9
    
#Función auxiliar que una vez no quedan segmentos en un barco, se asegura de sustituir sus 💥 por 🕳️
def hundirBarcos(eliminar, tablero, tablerofalso):
    key = str(eliminar)
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == key:
                tablerofalso[i][j] = '🕳️ '
            
#Función de ataque para el jugador 1, antes reutilizaba la misma función para todos los ataques, pero para tener más precisión de mensajes además de poder gestionar mejor los barcos restantes, hay una función para cada jugador tanto bot o persona sea
#La forma en la que funciona es que pide coordenadas mientras el ataque no sea válido, después, dependiendo de si ha hecho agua o contacto, restará un segmento y pondrá una 💥 o pondrá una 💧
def ataquej1(tablero, tableroReal):
    fila = 15
    col = 15
    print('Turno del Jugador 1')
    while verificarAtaque(fila, col, tablero) == False:
        fila = int(input('Jugador 1, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '. ':
            tablero[fila][col] = '💧'
        case _:
            tablero[fila][col] = '💥'
            key = str(tableroReal[fila][col])
            if key in barcosj2:
                barcosj2[key] -= 1

#Ataque para el jugador 2, igual que la anterior pero resta segmentos a los barcos del jugador 1
def ataquej2(tablero, tableroReal):
    fila = 15
    col = 15
    print('Turno del Jugador 2')
    while verificarAtaque(fila, col, tablero) == False:
        fila = int(input('Jugador 2, inserte la posición en eje y a la que atacar: '))
        col = int(input('Ahora en eje x: '))
    match tableroReal[fila][col]:
        case '. ':
            tablero[fila][col] = '💧'
        case _:
            tablero[fila][col] = '💥'
            key = str(tableroReal[fila][col])
            if key in barcosj1:
                barcosj1[key] -= 1

#Funcion para el jugador 1 cuando es un bot, simplemente calcula de forma aleatoria las coordenadas
def ataquebotj1(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) == False:
        fila = r.randint(0, len(tablero)-1)
        col = r.randint(0, len(tablero)-1)
    match tableroReal[fila][col]:
        case '. ':
            tablero[fila][col] = '💧'
        case _:
            tablero[fila][col] = '💥'
            key = str(tableroReal[fila][col])
            if key in barcosj2:
                barcosj2[key] -= 1

#Igual que la anterior pero para el jugador 2 cuando es un bot
def ataquebotj2(tablero, tableroReal):
    fila = 15
    col = 15
    while verificarAtaque(fila, col, tablero) == False:
        fila = r.randint(0, len(tablero)-1)
        col = r.randint(0, len(tablero)-1)
    match tableroReal[fila][col]:
        case '. ':
            tablero[fila][col] = '💧'
        case _:
            tablero[fila][col] = '💥'
            key = str(tableroReal[fila][col])
            if key in barcosj1:
                barcosj1[key] -= 1
    
#Función final que verifica si alguien ha ganado ya, mientras un jugador tenga al menos un barco que no tenga 9 segmentos, la partida continuará
def checkVictoria():
    global barcosj1, barcosj2
    ganador = True
    for i in barcosj1:
        if barcosj1[i] != 9:
            ganador = False
    if ganador == True:
        return 'J2'
    ganador = True
    for i in barcosj2:
        if barcosj2[i] != 9:
            ganador = False
    if ganador == True:
        return 'J1'
    return 'none'