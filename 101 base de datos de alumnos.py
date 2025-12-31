alumnos = {}

def agregar_alumno(nombre, edad, curso):
    global alumnos
    alumnos.update({len(alumnos)+1:{"nombre":nombre, "edad":edad, "curso":curso}})

def mostrarTodos():
    global alumnos
    print(alumnos)

def borrarAlumno(id):
    global alumnos
    alumnos.__delitem__(id)

def buscarEdad(edad):
    global alumnos
    for i in alumnos:
        if edad == alumnos[i]["edad"]:
            print(f"{i} : {alumnos[i]}")

def actualizar(id, nombre, edad, curso):
    global alumnos
    alumnos[id] = {"nombre":nombre, "edad":edad, "curso":curso}

flag = True
while flag == True:
    decision = int(input("-------ELECCION DE OPERACIÓN-------\n1)Agregar alumno\n2)Borrar alumno por id\n3)Buscar alumno por edad\n4)Mostrar toda la tabla\n5)Actualizar todos los datos por id\n6)Acabar\n"))
    match(decision):
        case 1:
            nombre = input("Inserta el nombre del alumno: ")
            edad = input("Inserta la edad del alumno: ")
            curso = input("Inserta el curso del alumno: ")
            agregar_alumno(nombre, edad, curso)
        case 2:
            id = int(input("Inserta el id a eliminar: "))
            borrarAlumno(id)
        case 3:
            edad = input("Inserta la edad del alumno: ")
            buscarEdad(edad)
        case 4:
            mostrarTodos()
        case 5: 
            id = int(input("Inserta el id del alumni: "))
            nombre = input("Inserta el nombre del alumno: ")
            edad = input("Inserta la edad del alumno: ")
            curso = input("Inserta el curso del alumno: ")
            actualizar(id, nombre, edad, curso)
        case 6:
            flag = False