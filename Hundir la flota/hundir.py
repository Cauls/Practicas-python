from funciones import *

def turnoJcJ():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2
    checkVictoria(mapaj1, mapaj2)
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    printTablero(mapaFalsoj2)
    input('Pulse intro cuando haya terminado de observar el resultado')
    printTablero(mapaFalsoj1)
    ataquej2(mapaFalsoj1, mapaj1)
    printTablero(mapaFalsoj1)
    input('Pulse intro cuando haya terminado de observar el resultado')

def turnoJcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2
    checkVictoria(mapaj1, mapaj2)
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    printTablero(mapaFalsoj2)
    input('Pulse intro cuando haya terminado de observar el resultado')
    printTablero(mapaFalsoj1)
    ataquebot(mapaFalsoj1, mapaj1)
    printTablero(mapaFalsoj1)
    input('Pulse intro cuando haya terminado de observar el resultado')

def turnoBcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2
    checkVictoria(mapaj1, mapaj2)
    printTablero(mapaFalsoj2)
    ataquebot(mapaFalsoj2, mapaj2)
    printTablero(mapaFalsoj2)
    input('Pulse intro cuando haya terminado de observar el resultado')
    printTablero(mapaFalsoj1)
    ataquebot(mapaFalsoj1, mapaj1)
    printTablero(mapaFalsoj1)
    input('Pulse intro cuando haya terminado de observar el resultado')

def partida():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2
    genBarcos(mapaj1)
    genBarcos(mapaj2)
    partidaModo = 0
    while partidaModo not in [1, 2, 3]:
        partidaModo = int(input('Elige la modalidad de la partida\n1)Jugador contra Jugador\n2)Jugador contra Maquina\n3)Maquina contra maquina'))
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


ganador = 'none'

mapaj1 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
mapaFalsoj1 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
mapaj2 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
mapaFalsoj2 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]


partida()


