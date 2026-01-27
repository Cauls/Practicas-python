from funciones import *

#Para el proyecto necesitaremos una matriz con lo que ve el oponente, y una matriz que tenga los barcos que están posicionados. Además, el ganador que sera none mientras no se haya ganado y la cuenta de los tiros de cada jugador
ganador = 'none'
tirosj1 = 0
tirosj2 = 0
mapaj1 = [
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
]
mapaFalsoj1 = [
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
]
mapaj2 = [
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
]
mapaFalsoj2 = [
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
]

#Primera función generalizada, reúne todas las funciones necesarias para desarrollar un turno de Jugador contra Jugador
#Imprime tablero de J2 -> Ataca el J1 -> comprueba los barcos y añade 1 a los tiros del J1 -> imprime tablero de J1 -> Ataca el J2 -> comprueba los barcos y añade un tiro al J2 -> imprime el tablero del J1 -> comprueba si alguien ha ganado
def turnoJcJ():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    ganador = checkVictoria()
    input('Pulse intro cuando haya terminado de observar el resultado')
    printTablero(mapaFalsoj1)
    ataquej2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)
    ganador = checkVictoria()
    input('Pulse intro cuando haya terminado de observar el resultado')


#Imprime tablero del bot -> Ataca el J1 -> comprueba los barcos y añade 1 a los tiros del J1 -> imprime tablero de J1 -> Ataca el bot -> comprueba los barcos y añade un tiro al bot -> imprime el tablero del J1 -> comprueba si alguien ha ganado
def turnoJcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    ganador = checkVictoria()
    input('Pulse intro cuando haya terminado de observar el resultado')
    ataquebotj2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)
    ganador = checkVictoria()
    input('Pulse intro cuando haya terminado de observar el resultado')

#Imprime tablero del botJ2 -> Ataca el botJ1 -> comprueba los barcos y añade 1 a los tiros del botJ1 -> imprime tablero de botJ1 -> Ataca el botJ2 -> comprueba los barcos y añade un tiro al botJ2 -> imprime el tablero del botJ1 -> comprueba si alguien ha ganado
def turnoBcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    ataquebotj1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    ganador = checkVictoria()
    ataquebotj2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)
    ganador = checkVictoria()

#Genera los mapas, pide al jugador que modo de juego quiere jugar y despues cicla turno tras turno del modo pedido mientras nadie haya ganado
def partida():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador
    genBarcos(mapaj1, mapaj2)
    partidaModo = 0
    while partidaModo not in [1, 2, 3]:
        partidaModo = int(input('Elige la modalidad de la partida\n1)Jugador contra Jugador\n2)Jugador contra Maquina\n3)Maquina contra maquina\n'))
    match partidaModo:
        case 1:
            while ganador == 'none':
                turnoJcJ()
        case 2:
            while ganador == 'none':
                turnoJcB()
        case 3:
            while ganador == 'none':
                turnoBcB()
            
#Comienza la partida y comenta quien ha ganado una vez haya acabado
partida()
print(f'Enhorabuena {ganador}, has ganado\nTiros del Jugador 1: {tirosj1}\nTiros del jugador 2: {tirosj2}')