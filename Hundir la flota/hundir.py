from funciones import *

ganador = 'none'
tirosj1 = 0
tirosj2 = 0
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

def turnoJcJ():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    ganador =checkVictoria()
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    input('Pulse intro cuando haya terminado de observar el resultado')
    printTablero(mapaFalsoj1)
    ataquej2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)
    input('Pulse intro cuando haya terminado de observar el resultado')

def turnoJcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    ganador = checkVictoria()
    printTablero(mapaFalsoj2)
    ataquej1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    input('Pulse intro cuando haya terminado de observar el resultado')
    ataquebotj2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)
    input('Pulse intro cuando haya terminado de observar el resultado')

def turnoBcB():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador, tirosj1, tirosj2
    ganador = checkVictoria()
    ataquebotj1(mapaFalsoj2, mapaj2)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj1 += 1
    printTablero(mapaFalsoj2)
    ataquebotj2(mapaFalsoj1, mapaj1)
    comprobarBarcos(mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2)
    tirosj2 += 1
    printTablero(mapaFalsoj1)

def partida():
    global mapaj1, mapaFalsoj1, mapaj2, mapaFalsoj2, ganador
    genBarcos(mapaj1, mapaj2)
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
            


partida()
print(f'Enhorabuena {ganador}, has ganado\nTiros del Jugador 1: {tirosj1}\nTiros del jugador 2: {tirosj2}')