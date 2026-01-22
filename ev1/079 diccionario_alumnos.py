diccionario = {
    "Alex" : [19, "2DAM"],
    "Wassim" : [21, "2DAM"],
    "Figue" : [19, "2DAM"],
    "Hugo" : [21, "2DAM"],
    "Misael" : [19, "2DAM"]
}

for clave, valor in diccionario.items():
    print(f"Alumno {clave} con edad {valor[0]} en el curso {valor[1]}")