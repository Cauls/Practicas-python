#Import de las funciones definidas en el archivo funciones.py, a su vez, abajo tenemos un diccionario vacio de jugadores junto a un diccionario de 20 palabras junto a sus pistas
from funciones import inicio, turno, asignarJugadores 
jugadores = {}
palabras = { 
    "Playa":"Bañador",
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

#Al comenzar la partida se usa asignarJugadores, esto pedirá la cantidad de jugadores junto al nombre de cada uno
asignarJugadores(jugadores)

#El comienzo de la partida, inicio asignará roles, le dará a cada uno su palabra e iniciará el bucle jugable
inicio(jugadores, palabras)

#Bucle muy sencillo, mientras haya al menos un impostor y mas de dos jugadores, la partida continuará, esto se debe a que los civiles perderán si hay tantos civiles como impostores y el impostor perderá si lo eliminan
while "Impostor" in jugadores.values() and len(jugadores) > 2:
    turno(jugadores)

#Sencillo condicional, si hay un impostor cuando la partida acaba, han ganado los impostores, si no, los civiles
if "Impostor" in jugadores.values():
    print("Victoria de los impostores")
else:
    print("Victoria de los civiles")