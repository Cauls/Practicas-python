#Import de las funciones definidas en el archivo funciones.py, a su vez, abajo tenemos un diccionario vacio de jugadores, un diccionario vacio donde ir almacenando la respuesta de cada jugador y un diccionario de 20 palabras junto a sus pistas
from funciones import inicio, turno, asignarJugadores, seleccionarDificultad
repetir = True
numRondas = 3
index = 0
jugadores = {}
dificultad = 0
frases = {}
palabras = { #Diccionario original
    "Playa": "Bañador",
    "Coche":"Carretera",
    "Microondas":"Ondas",
    "Videojuego":"Juego",
    "Tierra":"Planeta",
    "Manta":"Cuna",
    "Congelador":"Hielo",
    "Sartén":"Cacerola",
    "Cuchillo":"Tenedor",
    "Martillo":"Clavo",
    "Guante":"Calcetin",
    "Bufanda":"Braga del cuello",
    "Volcán":"Lava",
    "Cascada":"Rio",
    "Bosque":"Arbol",
    "Reloj":"Tiempo",
    "Tren":"Autobus",
    "Ascensor":"Escalera",
    "Panadero":"Quique",
    "Programador":"Copilot"
}
palabrasDificultad = {
    "Playa": ["Costa", "Bañador", "Agua"],
    "Coche": ["Vehiculo", "Carretera", "Combustible"],
    "Microondas":["Electrodomestico", "Ondas", "Calor"],
    "Videojuego":["Consola", "Juego", "Digital"]
}

while(repetir):
    #Al comenzar la partida se usa asignarJugadores, esto pedirá la cantidad de jugadores junto al nombre de cada uno
    asignarJugadores(jugadores, frases)
    while dificultad not in [1, 2, 3]:
        dificultad = int(input("Elige la dificultad del juego\nFacil: 6 rondas, pistas mas sutiles (más difícil para el impostor)\nNormal: el juego estándar, 3 rondas y pistas normales\nDifícil: solo 2 rondas, 2 impostores y pistas muy potentes\nElige con los números [Fácil 1, Normal 2, Difícil 3]"))
    numRondas = seleccionarDificultad(palabrasDificultad, dificultad)

    #El comienzo de la partida, inicio asignará roles, le dará a cada uno su palabra e iniciará el bucle jugable
    inicio(jugadores, dificultad)

    #Bucle muy sencillo, mientras haya al menos un impostor, no se superen el numero de rondas y  haya mas de dos jugadores, la partida continuará, esto se debe a que los civiles perderán si hay tantos civiles como impostores y el impostor perderá si lo eliminan
    while "Impostor" in jugadores.values() and len(jugadores) > 2 and index < numRondas:
        turno(jugadores, frases)
        index+=1

    #Sencillo condicional, si hay un impostor cuando la partida acaba, han ganado los impostores, si no, los civiles
    if "Impostor" in jugadores.values():
        print("Victoria de los impostores")
    else:
        print("Victoria de los civiles")
    index = 0
    dificultad = 0
    #Este ultimo switch es el que decidirá si se repite o no la partida, en caso de una S, la partida se repetirá, en caso de una N o cualquier otro valor, la partida no se repetirá
    eleccion = input("Quieres repetir la partida? S/N")
    match eleccion:
        case "S":
            repetir = True
        case "N":
            repetir = False
        case "Default":
            repetir = False
            print("No se repetirá la partida por entrada errónea")