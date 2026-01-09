import random

#Funcion para asignar jugadores, pide la cantidad de jugadores, e itera en un for x veces siendo x la cantidad de jugadores, cada iteración pide un jugador que será añadido sin rol alguno al diccionario
def asignarJugadores(jugadores):
    cantidad = 0
    while cantidad < 3:
        cantidad = int(input("Inserta el número de jugadores que van a jugar: "))
        if cantidad < 3: 
            print("El número mínimo de jugadores es 3")
    for i in range(cantidad):
        entrada = input("Inserta el nombre del jugador a añadir: ")
        jugadores[entrada] = "Nan"

#Según la cantidad de jugadores, se asigna un número aleatorio, el jugador en ese indice del diccionario será asignador como impostor, el resto como civiles
def impostor(jugadores):
    impostor = random.randint(0, len(jugadores)-1)
    index = 0
    for i in jugadores:
        if index == impostor:
            jugadores[i] = "Impostor"
        else:
            jugadores[i] = "Civil"
        index+=1

#Similar a la anterior funcion, en funcion de la cantidad de palabras en el diccionario, escogerá una al azar por indice y devolverá un array con la palabra y la pista
def selPalabra(palabras):
    palabra = ["", ""]
    elegida = random.randint(0, len(palabras)-1)
    index = 0
    for i in palabras:
        if index == elegida:
            palabra = [i, palabras[i]]
        index+=1
    return palabra

#El bucle de inicio, recorre todo el diccionario de jugadores e imprime la palabra o la pista a cada jugador dependiendo de que haya salido como impostor o como civil. También tengo un arte de ASCII ahi como introducción pero se rompe un poco la verdad
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

#Funcion que recibiendo la lista de jugadores y el jugador que se ha elegido para eliminar, decide si saltar la ronda o eliminar a un jugador del diccionario. Una vez lo elimina también notifica de que rol cumplía el jugador
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


#El bucle completo une al resto, este lo explicaré mas parte por parte
def turno(jugadores):
    restantes = ""      #<--Variable para almacenar mas adelante los jugadores que quedan
    for i in jugadores:
        restantes += f"{i} "    #<--Este bucle simplemente añade a restantes los jugadores que quedan
    eliminado = ""    #<--Variable vacía donde se ubicará el nombre del jugador votado
    for i in jugadores:
        input(f"Jugador {i}, inserte su frase: \n")     #<--Aquí se pide la frase de cada jugador
    while eliminado not in jugadores.keys() and eliminado != "Paso":    #<--Control de entrada, sigue preguntado constantemente a quien se vota mientras el jugador no exista en el diccionario ni se escriba 'Paso'
        print(f"Jugadores a eliminar: {restantes}")     #<--Imprime los jugadores restantes para no perderse a lo largo de la partida
        eliminado = input("Inserte el nombre del jugador votado o 'Paso' para saltar la ronda:\n")    #<--El input del voto
        if eliminado not in jugadores.keys():
            print(f"El jugador {eliminado} no se ha encontrado")    #<--De nuevo control de entrada, si el jugador no existe, avisará antes de repetir el bucle
    eliminar(jugadores, eliminado)    #<--Una vez se vota adecuadamente al jugador, este es mandado a eliminar
    
