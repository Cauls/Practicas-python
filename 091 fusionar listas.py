nombres = [
    "Figue",
    "Hugo",
    "Misa"
]
telefonos = [
    "666666666",
    "777777777",
    "888888888"
]
personas = {}
for i in range(len(nombres)):
    personas.update({nombres[i] : telefonos[i]})
print(personas)
