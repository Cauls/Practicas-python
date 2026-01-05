import random

def impostor(jugadores):
    impostor = random.randint(0, len(jugadores)-1)
    index = 0
    for i in jugadores:
        if index == impostor:
            jugadores[i] = "Impostor"
        else:
            jugadores[i] = "Civil"
        index+=1
    
def selPalabra(palabras):
    palabra = ["", ""]
    elegida = random.randint(0, len(palabras)-1)
    index = 0
    for i in palabras:
        if index == elegida:
            palabra = [i, palabras[i]]
        index+=1
    return palabra

def inicio(jugadores, palabras):
    print("=======================================================\n  _____ __  __ _____   ____   _____ _______ ____  _____ \n |_   _|  \/  |  __ \ / __ \ / ____|__   __/ __ \|  __ \ \n   | | | \  / | |__) | |  | | (___    | | | |  | | |__) | \n   | | | |\/| |  ___/| |  | |\___ \   | | | |  | |  _  / \n  _| |_| |  | | |    | |__| |____) |  | | | |__| | | \ \  \n |_____|_|  |_|_|     \____/|_____/   |_|  \____/|_|  \_\ \n=======================================================")
    impostor(jugadores)
    palabra = selPalabra(palabras)
    for i in jugadores:
        if jugadores[i] == "Civil":
            print(f"Jugador {i} es Civil\nSu palabra es {palabra[0]}\n\nPulse el intro para continuar")
            input("")
        if jugadores[i] == "Impostor":
            print(f"Jugador {i} es Impostor\nSu palabra es {palabra[1]}\n\nPulse el intro para continuar")
            input("")
        print("\n"*50)

def eliminar(jugadores, eliminado):
    if eliminado == "Paso":
        print("Se ha saltado la ronda")
    else:
        if jugadores[eliminado] == "Impostor":
            print(f"El jugador {eliminado} ha sido eliminado...")
            print(f"El jugador {eliminado} era un impostor")
            jugadores.pop(eliminado)
        else:
            print(f"El jugador {eliminado} ha sido eliminado...")
            print(f"El jugador {eliminado} era un civil")
            jugadores.pop(eliminado)



def turno(jugadores):
    eliminado = ""
    for i in jugadores:
        input(f"Jugador {i}, inserte su frase: \n")
    while eliminado not in jugadores.keys() and eliminado != "Paso":
        print(f"Jugadores a eliminar: {jugadores.keys()}")
        eliminado = input("Inserte el nombre del jugador votado o 'Paso' para saltar la ronda:\n")
    eliminar(jugadores, eliminado)
    
