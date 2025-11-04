from funciones import tiradaBot, tirar, imprimir, comprobar
#Aqui se hayan las únicas variables necesarias para el programa
#Ganador: Almacena el jugador que ha ganado (X o O). La mayor parte del tiempo se mantendrá con un string vacio para mantener el bucle ciclando. Sirve como herramienta de control de bucle, cerrándolo una vez se haya ganado.
ganador = ""
#Turno: Esta variable es la única responsable de decidir que simbolo juega en cada turno, altenando entre X y O dependiendo de que símbolo haya tirado en el anterior turno
turno = "X"
#Marco: Este array almacena el valor de cada casilla. Los espacios son los valores por defecto y se van cambiando por símbolos a medida que se vayan seleccionando por los jugadores
marco = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#X e Y: Estas variables sirven para elegir en que posición se quiere poner el símbolo como veremos mas adelante
X = 0
Y = 0
#Eleccion: Se encarga de elegir que modo de juego se va a jugar, se lo pide al jugador mediante un input
eleccion = int(input("Elige el modo de juego\n1)Jugador contra jugador\n2)Jugador contra máquina\n3)Maquina contra maquina"))

#Switch dedicado a decidir que modo de juego se jugará, si jugador contra jugador, jugador contra maquina o maquina contra maquina
match eleccion:
    case 1:
        #El modo jugador contra jugador, primero imprime el tablero
        imprimir(marco)
        #Mientras no haya ganador, tira con el jugador que haya seleccionado, imprime el tablero y cambia el jugador al que le toca ahora
        while ganador == "":
            tirar(turno, marco)
            imprimir(marco)
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            #Por ultimo, comprueba si se ha ganado o empatado ya
            ganador = comprobar(marco, ganador)
    case 2:
        #El modo jugador contra maquina, es muy parecido al anterior modo
        imprimir(marco)
        while ganador == "":
            #Aqui la mayor diferencia, es que comprueba que jugador es antes de decidir si va a tirar la maquina o el jugador, forzando siempre al jugador a ser la X
            if turno == "X":
                tirar(turno, marco)
                imprimir(marco)
                turno = "O"
            elif turno == "O":
                tiradaBot(turno, marco)
                imprimir(marco)
                turno = "X"
            ganador = comprobar(marco, ganador)
    case 3:
        imprimir(marco)
        while ganador == "":
            #Exactamente igual que con el jugador contra jugador pero haciendo que tire la maquina
            tiradaBot(turno, marco)
            imprimir(marco)
            if turno == "X":
                turno = "O"
            elif turno == "O":
                turno = "X"
            ganador = comprobar(marco, ganador)
    case default:
        #La consola advertirá de esto en caso de que la opción no sea reconocida como válida
        print("Opción no válida")