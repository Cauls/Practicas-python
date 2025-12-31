empleados = {
    "50565295W" : {
        "nombre" : "Álvaro",
        "puesto" : "Programador",
        "sueldo" : 2000
    },
    "50565295H" : {
        "nombre" : "Jose",
        "puesto" : "Programador",
        "sueldo" : 2000
    },
    "50565295M" : {
        "nombre" : "Hugo",
        "puesto" : "Programador",
        "sueldo" : 2000
    }
}

for i in empleados:
    print(f"{i} : {empleados[i]["nombre"]}")