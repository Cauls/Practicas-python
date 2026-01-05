from funciones import inicio, turno
jugadores = {
    "Figue":"Nan",
    "Misael":"Nan",
    "Sadesu":"Nan",
    "Wassim":"Nan"
}
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

inicio(jugadores, palabras)
while "Impostor" in jugadores.values() and len(jugadores) > 2:
    turno(jugadores)
if "Impostor" in jugadores.values():
    print("Victoria de los impostores")
else:
    print("Victoria de los civiles")